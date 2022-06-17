import logging
from utilities import subAPIs

class AssetsAPI(subAPIs.SubAPI):
  """This class is wrapping all functions related to assets and custom assets"""

  # GET functions
  def getAssetIds(self, catalogId, assetPath, artifact_type='data_asset'):
    '''
    Gets the Asset/Artifact Id from an asset path in a catalog.
    Returns one or many assets.
    Throws an exception if no  assets are found
    '''
    resJSON = self.mainAPI.search(f'entity.assets.connection_paths.keyword:{assetPath} AND metadata.artifact_type:{artifact_type} AND entity.assets.catalog_id:{catalogId}')
    assert resJSON['size'] > 0, 'No Asset Id found'
    return resJSON['rows'][0]['artifact_id']

  def getAssetById(self, assetId, catalogId):
    """ Gets an asset from its artifact id in a catalog
    Returns the assets JSON structure if found """
    return self.mainAPI._getJSON(f'/v2/assets/{assetId}?catalog_id={catalogId}')

  def getAssetTypes(self, catalogId):
    """ Gets all asset types setup in a catalog
    Returns the assets JSON structure if found """
    return self.mainAPI._getJSON(f'/v2/asset_types?catalog_id={catalogId}')

  def getAssetType(self, typeName, catalogId):
    """ Get all assets of a given type, e.g. data_asset
    Returns all assets that match the asset type """
    query = f'asset.name:{typeName}'
    payload = {
      "query": query,
      "limit": 10
    }
    return self.mainAPI._POST(f'/v2/asset_types/{typeName}/search?catalog_id={catalogId}', payload)

  def getAssetTypeRelationships(self, typeName):
    """ Get all assets of a given type, e.g. data_asset
    Returns all assets that match the asset type """
    return self.mainAPI._getJSON(f'/v2/asset_types/{typeName}/relationships')

  def getAssetRelationships(self, assetId, catalogId):
    """ Get all assets of a given type, e.g. data_asset
    Returns all assets that match the asset type """
    return self.mainAPI._getJSON(f'/v2/assets/{assetId}/relationships?catalog_id={catalogId}')

  def getAssetRelationshipTypes(self, assetId, catalogId):
    """ Get all assets of a given type, e.g. data_asset
    Returns all assets that match the asset type """
    return self.mainAPI._getJSON(f'/v2/assets/{assetId}/relationship_types?catalog_id={catalogId}')

  def getAssetAttributes(self, assetId, catalogId):
    """ Get all asset attributess of a given asset """
    return self.mainAPI._getJSON(f'/v2/assets/{assetId}/attributes?catalog_id={catalogId}')

  # PUT functions
  def createAssetAttributes(self, attributeName, catalog_id, payloadFile='assets/createassetattribute.json'):
    payload = self.mainAPI._loadPayload(payloadFile)
    return self.mainAPI._putJSON(f'/v2/asset_types/{attributeName}?catalog_id={catalog_id}', payload, statusCheck=200)

  def createAssetRelationship(self, relName, t_catalog_id, s_asset_id, t_asset_id):
    payload = {
      "relationship_targets": [
        {
          "catalog_id": t_catalog_id,
          "asset_id": t_asset_id
        }
      ]
    }
    return self.mainAPI._putJSON(f'/v2/assets/{s_asset_id}/relationships/{relName}?catalog_id={t_catalog_id}', payload, statusCheck=207)

  # POST functions
  def getListOfAllDataAssets(self, catalogId):
    """ Get list of all data assets in a given catalog
    Returns a list of all data assets """
    payload = {'query': '*:*'}
    return self.mainAPI._POST(f'/v2/asset_types/data_asset/search?catalog_id={catalogId}', payload)

  def getListOfAllAssetsByType(self, catalogId, assetType):
    """ Get a list of all assets of a given type in a given catalog
    Returns a list of all assets that match the asset type """
    payload = {'query': '*:*'}
    return self.mainAPI._POST(f'/v2/asset_types/{assetType}/search?catalog_id={catalogId}', payload)

  def getListOfBooksByAuthor(self, catalogId, assetType, author):
    """ Get a list of Books by a certain author in a given catalog
    Applies to custom type Book """
    payload = {'query': f'book.author.last_name:{author}'}
    return self.mainAPI._POST(f'/v2/asset_types/{assetType}/search?catalog_id={catalogId}', payload)

  def createAsset(self, catalogId, payload=None, payloadFile='asset_types/createCustomAssetBook.json'):  # example: book from Watson API Doc
    """Creates a custom asset in a catalog from the payloadfile provided"""
    if not payload and payloadFile:
      payload = self.mainAPI._loadPayload(payloadFile)
    assert payload, 'No payload passed in'
    return self.mainAPI._POST(f'/v2/assets?catalog_id={catalogId}', payload, statusCheck=201)

  def createAssetAttribute(self, assetId, catalogId, payloadFile='assets/createassetattribute.json'):
    """Creates an attributes to an asset in a catalog from the payloadfile provided"""
    payload = self.mainAPI._loadPayload(payloadFile)
    return self.mainAPI._POST(f'/v2/assets/{assetId}/attributes?catalog_id={catalogId}', payload, statusCheck=201)

  def createCustomAssetType(self, catalogId, payloadFile='asset_types/createCustomAssetTypeBook.json'):  # example: book from Watson API Doc
    """Creates a custom asset type in a catalog from the payloadfile provided"""
    payload = self.mainAPI._loadPayload(payloadFile)
    return self.mainAPI._POST(f'/v2/asset_types?catalog_id={catalogId}', payload, statusCheck=201)

  def createAssetRelationshipType(self, payloadFile='asset_relationship_types/createAssetRelationship.json'):
    """Creates a custom asset type in a catalog from the payloadfile provided"""
    payload = self.mainAPI._loadPayload(payloadFile)
    return self.mainAPI._POST(f'/v2/asset_relationship_types', payload, statusCheck=201)


  # PATCH functions
  def updateAsset(self, assetId, catalogId, payload=None, payloadFile=None, statusCheck=200):
    """   Updates a custom asset in a catalog from the payloadfile provided
  follow https://tools.ietf.org/html/rfc6902 """
    if payloadFile:
      payload = self.mainAPI._loadPayload(payloadFile)
    assert payload, 'No payload passed in'
    self.mainAPI._PATCH(f'/v2/assets/{assetId}?catalog_id={catalogId}', payload, statusCheck=statusCheck)

  def addTagToAsset(self, catalogId, assetId, tag):
    """ Adds a Tag to an asset """
    payload = [{'op': 'add', 'path': '/metadata/tags/-', 'value': tag}]
    self.updateAsset(assetId, catalogId, payload)

  def removeTagFromAsset(self, catalogId, assetId, idx):
    """ Removes a tag from an asset 
    Idx specifies the positional argument for the tag in the tag list
    could be evaluated as: idx = res["metadata"]["tags"].index('TAGNAME')"""
    payload = [{'op': 'remove', 'path': f'/metadata/tags/{idx}'}]
    self.updateAsset(assetId, catalogId, payload)

  def patchAssetAttribute(self, assetId, catalogId, attribute_key, payloadFile='asset_types/addtermtoasset.json'):
    """Creates a attributes to an asset in a catalog from the payloadfile provided"""
    payload = self.mainAPI._loadPayload(payloadFile)
    return self.mainAPI._PATCH(f'/v2/assets/{assetId}/attributes/{attribute_key}?catalog_id={catalogId}', payload, statusCheck=200)

  # DELETE functions
  def deleteAsset(self, assetId, catalogId):
    """Deletes an asset in a catalog"""
    return self.mainAPI._DELETE(f'/v2/assets/{assetId}?catalog_id={catalogId}', statusCheck=204)

  def deleteCustomAssetType(self, assetType, catalogId):
    """Deletes a custom asset type in a catalog"""
    return self.mainAPI._DELETE(f'/v2/asset_types/{assetType}?catalog_id={catalogId}', statusCheck=204)
