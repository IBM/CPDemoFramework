from utilities import subAPIs
import logging

class RefDataAPI(subAPIs.SubAPI):
  """This class represents all functions related to reference data"""

  def getListOfRefData(self, refDataName):
    """Get a list of reference data sets"""
    return self.mainAPI.search(f'metadata.name.keyword:{refDataName} AND metadata.artifact_type:reference_data')

  # GET functions
  def getRefData(self, artifact_id, version_id=None):
    """Get reference data from a given set"""
    if not version_id:
      version_id = self.mainAPI.getVersionId(artifact_id)
    allRefdata = self.mainAPI._getJSON(f'/v3/reference_data/{artifact_id}/versions/{version_id}?values_offset=0&values_limit=1')
    logging.info(allRefdata)
    return self._expandRefDataWithValues(artifact_id, version_id, allRefdata)

  def getRefDataCSV(self, artifact_id, filename, version_id=None):
    """Export a CSV file containing reference data values of a given reference data set"""
    if not version_id:
      version_id = self.mainAPI.getVersionId(artifact_id)
    endpoint = f'/v3/reference_data/{artifact_id}/versions/{version_id}/values'
    self.mainAPI._getFile(endpoint, filename)

  # POST functions
  def createRefData(self, payloadFile='reference_data/createRefData.json', skip_workflow=True):
    """ Create new reference data
    This can create a new set with or without reference data values"""
    payload = self.mainAPI._loadPayload(payloadFile)
    endpoint = f'/v3/reference_data/?skip_workflow_if_possible={skip_workflow}'
    return self.mainAPI._POST(endpoint, payload, statusCheck=201)

  # PUT functions
  def loadRefDataFromCSV(self, artifact_id, filename, version_id=None, skip_workflow=True):
    """Import reference data values from a csv file into a given reference data set"""
    if not version_id:
      version_id = self.mainAPI.getVersionId(artifact_id)
    files = {'file': (filename, open(filename, 'rb'), 'text/csv')}
    endpoint = f'/v3/reference_data/{artifact_id}/versions/{version_id}/values/import?code=code&value=value&description=description&skip_workflow_if_possible={skip_workflow}'
    self.mainAPI._putFile(endpoint, files=files, contentType='multipart/form-data', statusCheck=202)

  # DELETE functions
  def deleteRefData(self, artifact_id, version_id=None, skip_workflow=True):
    """Delete a given reference data set"""
    if not version_id:
      version_id = self.mainAPI.getVersionId(artifact_id)
    endpoint = f'/v3/reference_data/{artifact_id}/versions/{version_id}?skip_workflow_if_possible={skip_workflow}'
    self.mainAPI._DELETE(endpoint)

  # Functions for mass reference data extraction
  def _expandRefDataWithValues(self, artifact_id, version_id, allRefdata):
    """Iterates over the list of reference data values in a given set"""
    for i in range(allRefdata['entity']['rds_values_total_counts']):
      value = self._extractRefDataValue(f'/v3/reference_data/{artifact_id}/versions/{version_id}?values_offset={i + 1}&values_limit=1')
      allRefdata['entity']['rds_values']['resources'].extend(value)
    return allRefdata

  def _extractRefDataValue(self, endpoint):
    """Get a reference data value"""
    resJSON = self.mainAPI._getJSON(endpoint)
    logging.info(resJSON['entity']['rds_values'])
    return resJSON['entity']['rds_values']['resources']
