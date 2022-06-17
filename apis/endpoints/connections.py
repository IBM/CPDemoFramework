from utilities import subAPIs

class ConnectionsAPI(subAPIs.SubAPI):
  """This class represents all functions related to Connections"""

  # GET functions
  def getListOfConnections(self, catalog_id):
    """Get a list of Connections in a givven catalog"""
    return self.mainAPI._getJSON(f'/v2/connections?catalog_id={catalog_id}')

  def getListOfSSLConnections(self, catalog_id, name):
    """Get a list of SSL connections in a given catalog"""
    return self.mainAPI._getJSON(f'/v2/connections?catalog_id={catalog_id}&entity.properties.ssl=true&entity.name={name}')

  def getConnection(self, connection_id, catalog_id):
    """Get a connection by a given id in a given catalog"""
    return self.mainAPI._getJSON(f'/v2/connections/{connection_id}?catalog_id={catalog_id}')

  def getConnectionAssets(self, connection_id, catalog_id):
    """Get a list of assets that belong to a connection by a given id in a given catalog"""
    return self.mainAPI._getJSON(f'/v2/connections/{connection_id}/assets?catalog_id={catalog_id}')
