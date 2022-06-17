import logging
from utilities import subAPIs

class DataRequestAPI(subAPIs.SubAPI):
  """This class represents all functions dealing with Data Requests"""

  # GET functions
  def getDataRequests(self, SelectBy=None, Value=None):
    """Reading out data requests with or without filtering"""
    if not SelectBy:
      # Returns all data requests stored in the system
      return self.mainAPI._getJSON('/zen-data-ui/v1/datarequest')
    else:
      # Returns filtered set of data requests
      return self.mainAPI._getJSON(f'/zen-data-ui/v1/datarequest?SelectBy={SelectBy}&Value={Value}')

  # DELETE functions
  def deleteDataRequest(self, id):
    """Deletes a data requests stored in the system by its id"""
    return self.mainAPI._DELETE(f'/zen-data-ui/v1/datarequest/{id}')

  def _iterateDelete(self, res):
    """Iterates over an array of requestObj as contained in response from getDataRequest function"""
    for dr in res["requestObj"]:
      id = dr["Id"]
      logging.info(dr["Title"])
      logging.debug(id)
      self.deleteDataRequest(id)

  def deleteAllDataRequestsByState(self, status):
    """Gets all data requests of a given status and deletes these"""
    res = self.getDataRequests('State', status)
    self._iterateDelete(res)

  def deleteAllDataRequestsByUser(self, user):
    """Gets all data requests from a given user and deletes these"""
    res = self.getDataRequests('AssignedTo', user)
    self._iterateDelete(res)

 # POST functions
  def createDataRequest(self, payloadFile='datarequest/postnewrequest.json'):
    """Create a new data request from a json payload file"""
    payload = self.mainAPI._loadPayload(payloadFile)
    endpoint = f'/zen-data-ui/v1/datarequest'
    return self.mainAPI._POST(endpoint, payload, statusCheck=200)