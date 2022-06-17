from logging import debug, info
from utilities import csvProcessing, subAPIs
import ast

class CategoriesAPI(subAPIs.SubAPI):
  """This class represents all functions related to categories"""

  # GET functions
  def getListOfCategories(self):
    """Get a list of all categories"""
    return self.mainAPI.search('metadata.artifact_type:category')

  def getListOfTopLevelCategories(self):
    """Get a list of all top level categories"""
    return self.mainAPI.search('metadata.artifact_type:category NOT categories.primary_category_name:*')


  def getListOfCategoriesForParentById(self, parentId):
    """Get a list of all categories underneath one parent category as indicated by its id"""
    return self.mainAPI.search(f'metadata.artifact_type:category AND categories.primary_category_id:{parentId}')

  def getCategoryByName(self, category):
    """Get a Category by a given name
    This function may return many categories"""
    return self.mainAPI.search(f'metadata.artifact_type:category AND metadata.name.keyword:{category}')

  def getCategoryByPath(self, catpath):
    """Get a Category by a given path
    Path should follow the structure /top/sub1/sub2
    This function returns exactly one category"""
    cat = catpath.split('/')
    if catpath.startswith("/"):
      cat.pop(0)
    rescat = ''
    parentId = ''
    for lvl in cat:
        rescat = ''
        if lvl == cat[0]:
            cats = self.getListOfTopLevelCategories()["rows"]
            for c in cats:
                if lvl == c["metadata"]["name"]:
                    parentId = c["artifact_id"]
                    rescat = c
        else:
            cats = self.getListOfCategoriesForParentById(parentId)["rows"]
            for c in cats:
                if lvl == c["metadata"]["name"]:
                    parentId = c["artifact_id"]
                    rescat = c
    return rescat

  # DELETE functions
  # TODO: delete other artifacts as well
  def deleteCategory(self, guid):
    """Delete a category by a given id
    Currently requires that there are no artifacts stored in that category anymore"""
    return self.mainAPI._DELETE(f'/v3/categories/{guid}')

 # POST functions
  def createCategory(self, payloadFile='categories/createCategory.json'):
    """Create a new term from a json payload file"""
    payload = self.mainAPI._loadPayload(payloadFile)
    endpoint = f'/v3/categories'
    return self.mainAPI._POST(endpoint, payload, statusCheck=201)

  def createCategory(self, categoryName, categoryShortDescription, categoryLongDescription):
    """Create a new category from a name, short and long description"""
    payload = {
      'long_description': categoryLongDescription,
      'name': categoryName,
      'short_description': categoryShortDescription
    }
    endpoint = f'/v3/categories'
    return self.mainAPI._POST(endpoint, payload, statusCheck=201)

  def categories2Table(self, categoriesJSON):
    """creates a table from a list of categories
    Args:
        categoriesJSON (dict): JSON formatted output of the WKC API for a list of categories
    Returns:
      pandas.DataFrame: table of categories
    """
    assert categoriesJSON['size'] > 0, 'No Categories found'
    return csvProcessing.items2Table(self._addCategory2Table, categoriesJSON['rows'])

  def _addCategory2Table(self, table, categoriesJSON):
    debug(categoriesJSON)
    artifacts = categoriesJSON['entity']['artifacts']
    metadata = categoriesJSON['metadata']
    debug(metadata)
    row = self._creatCategoriesRow(artifacts, metadata)
    row = self._addDescriptionIfPresent(row, metadata)
    return table.append(row, ignore_index=True)

  def _creatCategoriesRow(self, artifacts, metadata):
    return {
      'artifact_id': artifacts['artifact_id'],
      'name': metadata['name'],
      'steward_ids': metadata['steward_ids'],
      'tags': metadata['tags']
    }

  def _addDescriptionIfPresent(self, row, metadata):
      if 'description' in metadata.keys():
        row['description'] = metadata['description']
      return row

  def categories2CSV(self, categoriesJSON, filePath):
    """creates a csv file of terms
    Args:
        itemsJSON (dict): JSON formatted output of the WKC API for a list of terms
        filePath (str): name or filepath for the creation of the csv file
    """
    csvProcessing.items2CSV(self._addCategory2Table, categoriesJSON['rows'], filePath)

 # Functions for mass category updates
  def _getCategoryPayload(self, categoryRow, revision, steward_ids, tags):
    """Construct a category payload from some of its parameters"""
    return {
      'long_description': categoryRow['description'],
      'name': categoryRow['name'],
      'steward_ids': steward_ids,
      'tags': tags,
    }

  def _updateCategoryFromRow(self, categoryRow):
    """Updates a category with the content from the table"""
    steward_ids = ast.literal_eval(categoryRow['steward_ids'])
    tags = ast.literal_eval(categoryRow['tags'])
    version_id = self.mainAPI.getVersionId(categoryRow['artifact_id'])
    revision = self.getCategory(categoryRow['artifact_id'], version_id)["metadata"]["revision"]
    payload = self._getCategoryPayload(categoryRow, revision, steward_ids, tags)
    self.updateCategory(categoryRow['artifact_id'], payload, version_id)

  def updateCategoriesFromTable(self, categoryTable):
    """Iterates over the terms contained in a table"""
    for _, categoryRow in categoryTable.iterrows():
      self._updateCategoryFromRow(categoryRow)

  def getCategory(self, artifact_id, version_id=None):
    """ Get a category
    If version id is provided then that version is returned, else the latest version is returned"""
    if not version_id:
      version_id = self.mainAPI.getVersionId(artifact_id)
    return self.mainAPI._getJSON(f'/v3/categories/{artifact_id}')

  # PATCH functions
  def updateCategory(self, artifact_id, payload, version_id=None, skip_workflow=True):
    """Update a category with a payload provided"""
    if not version_id:
      version_id = self.mainAPI.getVersionId(artifact_id)
    self.mainAPI._PATCH(f'/v3/categories/{artifact_id}', payload)
