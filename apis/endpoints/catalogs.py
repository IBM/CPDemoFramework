import logging
from utilities import subAPIs

class CatalogsAPI(subAPIs.SubAPI):
  """ This class represents all functions related to catalogs """

  # GET functions
  def getDefaultCatalog(self):
    """ Returns the default catalog """
    return self.mainAPI._getJSON('/v2/catalogs/default')

  def getPlatformAssetCatalog(self):
    """ Returns the Platform Assets catalog """
    return self.mainAPI._getJSON('/v2/catalogs/ibm-global-catalog')

  def getDefaultCatalogId(self):
    """ Gets the Default Catalog
    Returns catalog_id if default catalog was found
    Returns an exception if default catalog was not found """
    resJSON = self.getDefaultCatalog()
    try:
      return resJSON['metadata']['guid']
    except:
      raise ValueError('No Default Catalog found')

  def getCatalogs(self):
    """ Returns all catalogs """
    return self.mainAPI._getJSON('/v2/catalogs')

  def getCatalog(self, catalog_id):
    """ Returns one catalog """
    return self.mainAPI._getJSON(f'/v2/catalogs/{catalog_id}')

  def getCatalogProperties(self, catalog_id):
    """ Returns all catalog properties  """
    return self.mainAPI._getJSON(f'/v2/catalogs/{catalog_id}/properties')

  def getCatalogMembers(self, catalog_id):
    """ Returns all catalog members """
    return self.mainAPI._getJSON(f'/v2/catalogs/{catalog_id}/members')

  def getCatalogMembershipByUserId(self, catalog_id, member_id):
    """ Returns catalogs membership for a user """
    return self.mainAPI._getJSON(f'/v2/catalogs/{catalog_id}/members/{member_id}')

  def getCatalogNames(self):
    """ Gets a list of all Catalog names
    Returns catalog names for all catalogs found """
    resJSON = self.mainAPI._getJSON('/v2/catalogs')
    logging.info(resJSON['catalogs'])
    catlist = []
    for obj in resJSON['catalogs']:
      logging.info(f'Catalog Name is: {obj["entity"]["name"]} + GUID is: {obj["metadata"]["guid"]}')
      catlist.append(obj['entity']['name'])
    return catlist

  def getCatalogIdByName(self, catalogName):
    """ Gets a Catalog by a given name
    Returns catalog_id if catalog name was found
    Returns an exception if catalog name was not found """
    # Invoke Endpoint
    resJSON = self.getCatalogs()
    catalogId = [obj for obj in resJSON['catalogs'] if(obj['entity']['name'] == catalogName)]
    logging.debug(catalogId)
    try:
      return catalogId[0]['metadata']['guid']
    except:
      raise ValueError('No Catalog found')
