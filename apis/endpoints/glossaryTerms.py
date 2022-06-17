import ast
import csv
from logging import debug, info
from utilities import csvProcessing, subAPIs

class TermsAPI(subAPIs.SubAPI):
  """This class represents all functions related to glossary terms"""
  def __init__(self, mainAPI=None):
    super().__init__(mainAPI)

  # GET functions
  def getListOfTerms(self, termName):
    """Gets a list of published terms by keyword"""
    return self.mainAPI.search(f'metadata.name.keyword:{termName} AND metadata.artifact_type:glosary_term')

  def getListOfTermDrafts(self, limit=200):
    """Gets a list of Term drafts"""
    return self.mainAPI._getJSON(f'/v3/governance_artifact_types/glossary_term?limit={limit}')

  def getListOfTermDraftsByCategory(self, category, limit=200):
    """Gets a list of Term drafts in a given category"""
    res = self.mainAPI._getJSON(f'/v3/governance_artifact_types/glossary_term?limit={limit}')
    lst = []
    if res["count"] > 0:
      for term in res["resources"]:
        if term["parent_category"]["name"] == category:
          lst.append(term)
    return lst

  def getTerms(self, status, limit):
    """Get a list of terms in a given status"""
    termsJSON = self.mainAPI._getJSON(f'/v3/glossary_terms?status={status}&limit={limit}')
    allTerms = termsJSON['resources']
    while 'next' in termsJSON:
      termsJSON = self.mainAPI._getJSON(termsJSON['next']['href'])
      allTerms.extend(termsJSON['resources'])
    return allTerms

  def getPublishedVersionsOfTerm(self, artifact_id):
    """Get the published version of a given term"""
    return self.mainAPI._getJSON(f'/v3/glossary_terms/{artifact_id}/versions?status=PUBLISHED')

  def getDraftVersionsOfTerm(self, artifact_id):
    """Get the draft version of a given term"""
    return self.mainAPI._getJSON(f'/v3/glossary_terms/{artifact_id}/versions?status=DRAFT')

  def getTerm(self, artifact_id, version_id=None):
    """ Get a term
    If version id is provided then that version is returned, else the latest version is returned"""
    if not version_id:
      version_id = self.mainAPI.getVersionId(artifact_id)
    return self.mainAPI._getJSON(f'/v3/glossary_terms/{artifact_id}/versions/{version_id}?all_parents=true')

  # POST functions
  def createTerm(self, payloadFile='glossary_terms/createTerm.json', skip_workflow=True):
    """Create a new term from a json payload file"""
    payload = self.mainAPI._loadPayload(payloadFile)
    endpoint = f'/v3/glossary_terms?skip_workflow_if_possible={skip_workflow}'
    return self.mainAPI._POST(endpoint, payload, statusCheck=201)

  def createTerm(self, termAbbreviations, termName, termShortDescription, termLongDescription, skip_workflow=True):
    """Create a new term from a json payload file"""
    payload = [
  {
    "abbreviations": termAbbreviations,
    "long_description": termLongDescription,
    "name": termName,
    "short_description": termShortDescription
  }
]
    endpoint = f'/v3/glossary_terms?skip_workflow_if_possible={skip_workflow}'
    return self.mainAPI._POST(endpoint, payload, statusCheck=201)

  # PATCH functions
  def updateTerm(self, artifact_id, payload, version_id=None, skip_workflow=True):
    """Update a term with a payload provided"""
    if not version_id:
      version_id = self.mainAPI.getVersionId(artifact_id)
    self.mainAPI._PATCH(f'/v3/glossary_terms/{artifact_id}/versions/{version_id}?skip_workflow_if_possible={skip_workflow}', payload)

  def patchGlossaryTerm(self, artifact_id, custom_attribute_value, version_id=None, skip_workflow=True):
    """Update a given term with a custom attribute"""
    if not version_id:
      version_id = self.mainAPI.getVersionId(artifact_id)
    payload = {
      'revision': '1',
      'custom_attributes': [{
          'custom_attribute_definition_id': '9d32bf51-4c2c-49b1-ab8f-cc82fe90785d',
          'name': 'Enterprise Data ID',
          'values': [{'value': custom_attribute_value}]
      }]
    }
    self.mainAPI._PATCH(f'/v3/glossary_terms/{artifact_id}/versions/{version_id}?skip_workflow_if_possible={skip_workflow}', payload)
    info('Term patched')

  def patchTermsWithCustomAttribute(self, filename):
    """Patch terms from a list with a custom attribute definition"""
    with open(filename, newline='') as csvFile:
      reader = csv.DictReader(csvFile, delimiter=',')
      for row in reader:
        info(row['Asset Name'], row['Parent Category'], row['Enterprise Data ID'])
        # Go fetch the artifact_id and version_id for each of the combination of term and parent category
        termIds = self.mainAPI.search(f'metadata.name.keyword:{row["Asset Name"]} AND categories.primary_category_name.keyword:{row["Parent Category"]} AND metadata.artifact_type:glossary_term')
        artifact_id = termIds['artifact_id']
        version_id = termIds['entity']['artifacts']['version_id']
        # Patch the term with the new Enterprise ID
        self.patchGlossaryTerm(artifact_id, version_id, row['Enterprise Data ID'])
    info('Term updates done!')

  # DELETE functions
  def deleteTerm(self, artifact_id, version_id=None, skip_workflow=True):
    """Delete a given term"""
    if not version_id:
      version_id = self.mainAPI.getVersionId(artifact_id)
    if skip_workflow:
      return self.mainAPI._DELETE(f'/v3/glossary_terms/{artifact_id}/versions/{version_id}?skip_workflow_if_possible={skip_workflow}', statusCheck=204)
    else:
      return self.mainAPI._DELETE(f'/v3/glossary_terms/{artifact_id}/versions/{version_id}?skip_workflow_if_possible={skip_workflow}', statusCheck=201)

  def deleteAllTermDrafts(self):
    """Delete all Draft Terms"""
    resJSON = self.mainAPI._getJSON('/v3/governance_artifact_types/glossary_term?limit=200')
    # iterate over list of terms
    for term in resJSON['resources']:
      debug(term)
      self.deleteTerm(term["artifact_id"], term["version_id"], skip_workflow=True)

  def deleteAllTermsFromCategory(self, category):
    """Delete all Published Terms in a given category"""
    res = self.mainAPI.search(f'categories.primary_category_name.keyword:{category} AND metadata.artifact_type:glossary_term')
    # iterate over list of terms
    for term in res['rows']:
      artifact_id = term["entity"]["artifacts"]["artifact_id"]
      version_id = term["entity"]["artifacts"]["version_id"]
      info(term["metadata"]["name"])
      debug(artifact_id)
      debug(version_id)
      self.deleteTerm(artifact_id, version_id, skip_workflow=True)
    return res

  # Functions for mass term updates
  def _getTermPayload(self, termRow, revision, steward_ids, tags):
    """Construct a term payload from some of its parameters"""
    return {
      'revision': revision,
      'long_description': termRow['description'],
      'name': termRow['name'],
      'steward_ids': steward_ids,
      'tags': tags,
    }

  def _updateTermFromRow(self, termRow):
    """Updates a term with the content from the table"""
    steward_ids = ast.literal_eval(termRow['steward_ids'])
    tags = ast.literal_eval(termRow['tags'])
    version_id = self.mainAPI.getVersionId(termRow['artifact_id'])
    revision = self.getTerm(termRow['artifact_id'], version_id)["metadata"]["revision"]
    payload = self._getTermPayload(termRow, revision, steward_ids, tags)
    self.updateTerm(termRow['artifact_id'], payload, version_id)

  def updateTermsFromTable(self, termTable):
    """Iterates over the terms contained in a table"""
    for _, termRow in termTable.iterrows():
      self._updateTermFromRow(termRow)

  def _addTerm2Table(self, table, termJSON):
    debug(termJSON)
    artifacts = termJSON['entity']['artifacts']
    metadata = termJSON['metadata']
    debug(metadata)
    row = self._creatTermsRow(artifacts, metadata)
    row = self._addDescriptionIfPresent(row, metadata)
    return table.append(row, ignore_index=True)

  def _addDescriptionIfPresent(self, row, metadata):
      if 'description' in metadata.keys():
        row['description'] = metadata['description']
      return row

  def _creatTermsRow(self, artifacts, metadata):
    return {
      'artifact_id': artifacts['artifact_id'],
      'name': metadata['name'],
      'steward_ids': metadata['steward_ids'],
      'tags': metadata['tags']
    }

  def terms2Table(self, termsJSON):
    """creates a table from a list of terms
    Args:
        termsJSON (dict): JSON formatted output of the WKC API for a list of terms
    Returns:
      pandas.DataFrame: table of terms
    """
    assert termsJSON['size'] > 0, 'No Terms found'
    return csvProcessing.items2Table(self._addTerm2Table, termsJSON['rows'])

  def terms2CSV(self, termsJSON, filePath):
    """creates a csv file of terms
    Args:
        itemsJSON (dict): JSON formatted output of the WKC API for a list of terms
        filePath (str): name or filepath for the creation of the csv file
    """
    csvProcessing.items2CSV(self._addTerm2Table, termsJSON['rows'], filePath)
