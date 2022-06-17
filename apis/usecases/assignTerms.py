import apis
from utilities import subAPIs
import logging
import csv

class AssignTermsAPI(subAPIs.SubAPI):
  """This class represents all functions related to assigning terms"""
  def __init__(self, mainAPI=None):
    super().__init__(mainAPI)
    self.assetsAPI = apis.AssetsAPI(self.mainAPI)
    self.catalogsAPI = apis.CatalogsAPI(self.mainAPI)

  # TODO: Understand this function
  def assignTermToColumnWKC(self, parentCategory, term, catalog, schemaAssetPath, column):
    catalogId = self.catalogsAPI.getCatalogIdByName(catalog)
    termInfo = self.mainAPI.search(f'metadata.name.keyword:{term} AND categories.primary_category_name.keyword:{parentCategory} AND metadata.artifact_type:glossary_term')
    termId = termInfo['entity']['artifacts']['artifact_id']
    termName = termInfo['metadata']['name']
    assetId = self.assetsAPI.getAssetId(catalog, schemaAssetPath)

    logging.info(f'termid:{termId}')
    payload = [{
      'op': 'add',
      'path': f'/{column}',
      'value': {'column_terms': [{
        'term_id': termId,
        'term_display_name': termName
      }]},
      'attribute': 'column_info'
    }]
    self.mainAPI._PATCH(f'/v2/assets/{assetId}/attributes/column_info?catalog_id={catalogId}', payload)

  # TODO: Understand this function
  def assignTermsToColumnsWKC(self, csvTermSourceFile):
    with open(csvTermSourceFile, newline='') as csvFile:
      reader = csv.DictReader(csvFile, delimiter=',')
      list_of_dicts = list(reader)
    for row in list_of_dicts:
      self.assignTermToColumnWKC(row['Parent Category'], row['Term'], row['Catalog'], row['Schema/Asset Path'], row['Column'])
    return list_of_dicts
