""""""
from distutils.log import info
from utilities import helper
from decouple import config
import logging
import json
import os
import requests
from requests.packages import urllib3

class MainAPI():
  """Watson Knowledge Catalog (WKC) Application Programmer Interface (API). This class is the main class holding functions to access the CP4D backend"""
  def __init__(self):
    self.baseURL = f'https://{config("TZHOSTNAME")}'
    logging.info(f'URL: {self.baseURL}')
    self.headers = {'cache-control': 'no-cache'}
    self.session = requests.Session()
    self._authorize()
    self.payloadsPath = helper.getPayloadsPath()

  # Authorization
  def _authorize(self):
    """Core function"""
    try:
      return self._tryAuthorize()
    except Exception as e:
      raise ValueError(f'Error authenticating: {e}')

  def _tryAuthorize(self):
    """Slipping in the credentials
    Executing the endpoint
    Checking for successful response"""
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = self.session.post(f'{self.baseURL}/icp4d-api/v1/authorize', headers=self.headers, json={'username': config('WKCUSER'), 'password': config('PASSWORD')}, verify=False)
    assert res.status_code == 200, f'{res.status_code}: {res.text}'
    resJSON = res.json()
    return self._authorizeHeaders(resJSON)

  def _authorizeHeaders(self, resJSON):
    """Injecting the Token into the Header"""
    access_token = resJSON['token']
    self.headers['Authorization'] = f'Bearer {access_token}'
    logging.info(f'HEADERS: {self.headers}')

  # Requests
  def _getJSON(self, endpoint, payload=None, statusCheck=200):
    """GET requests that use and return a JSON structures"""
    res = self._GET(endpoint, payload, 'application/json', statusCheck)
    logging.debug(f'Response: {res.text}')
    return res.json()

  def _getFile(self, endpoint, filename, statusCheck=200):
    """GET requests that return a file"""
    res = self._GET(endpoint, None, 'application/octet-stream', statusCheck)
    logging.debug(res)
    with open(filename, 'wb') as f:
      f.writelines(res)
    logging.info(res.text)

  def _GET(self, endpoint, payload, contentType, statusCheck):
    """The generic GET function, getJSON or getFile should be preferably used"""
    return self._createRequest(self.session.get, endpoint, contentType, statusCheck, payload=payload)

  def _POST(self, endpoint, payload, contentType='application/json', statusCheck=200):
    """POST requests that use a JSON payload"""
    res = self._createRequest(self.session.post, endpoint, contentType, statusCheck, payload=payload)
    logging.debug(f'Response Headers: {res.headers}')
    logging.debug(f'Response Text: {res.text}')
    if 'Content-Length' in res.headers:
      if res.headers['Content-Length'] != '0':
        return res.json()
      else:
        return {}
    else:
      if res.headers['Content-Type'] == 'application/json':
        return res.json()
      else:
        return {}

  def _PATCH(self, endpoint, payload, contentType='application/json', statusCheck=200):
    """PATCH requests that use a JSON payload, but return nothing"""
    res = self._createRequest(self.session.patch, endpoint, contentType, statusCheck, payload=payload)
    logging.info(res.text)

  def _putFile(self, endpoint, files, contentType='application/json', statusCheck=200):
    """PUT requests that use a JSON payload, but return nothing"""
    res = self._createRequest(self.session.put, endpoint, contentType, statusCheck, files=files)
    logging.info(res.text)

  def _putJSON(self, endpoint, payload, contentType='application/json', statusCheck=200):
    """PUT requests that use a JSON payload, and returns JSON"""
    return self._createRequest(self.session.put, endpoint, contentType, statusCheck, payload=payload)

  def _DELETE(self, endpoint, contentType='application/json', statusCheck=200):
    """DELETE requests that use a JSON payload"""
    res = self._createRequest(self.session.delete, endpoint, contentType, statusCheck)
    logging.debug(f'Res: {res}')
    if res.headers['Content-Length'] != '0':
      return res.json()
    else:
      return {}

  def _createRequest(self, requestFun, endpoint, contentType, statusCheck, payload=None, files=None):
    """Generic Request function for all request types"""
    url = self.baseURL + endpoint
    headers = self._createContentTypeHeaders(contentType)
    self._logAPIFunctionInfo(headers, endpoint, payload, files)
    res = helper.sendRequestWithPayload(requestFun, url, headers, payload=payload, files=files)
    logging.debug(f'Res: {res}')
    assert res.status_code == statusCheck, f'{res.status_code}: {res.text}'
    return res

  def _createContentTypeHeaders(self, contentType):
    """Setting the content type in the request header"""
    headers = self.headers.copy()
    if contentType:
      headers['Content-Type'] = contentType
    #headers['Accept'] = "*/*"
    #headers['Accept-Encoding'] = "gzip, deflate, br"
    #headers['Connection'] = "keep-alive"
    return headers

  def _logAPIFunctionInfo(self, headers, endpoint, payload, files):
    """Central logging of the various session parameters"""
    logging.debug(f'URL: {self.baseURL}')
    logging.debug(f'HEADERS: {headers}')
    logging.info(f'{helper.getRequestName()} {endpoint}')
    if payload:
      logging.info(f'PAYLOAD: {payload}')
    if files:
      logging.info(f'FILES: {files}')

  # API functions
  def search(self, searchString, payloadFile=None):
    """Searches WKC
    Can be based on lucene parser syntax usable for many search needs
    Can also take a complex JSON payload usable for very specific search needs
    Args:
        searchString (str): Search Phrase. Lucene Parser Syntax can be applied for filtering (https://lucene.apache.org/core/2_9_4/queryparsersyntax.html)
    Returns:
        dict: Search result with `dict_keys(['size', 'rows', 'aggregations'])`
    """
    if payloadFile:
      payload = self._loadPayload(payloadFile)
    else:
      payload = None
    return self._getJSON(f'/v3/search?query={searchString}', payload)

  def executeCAMSHealthCheck(self):
    """Executes a CAMS health check"""
    return self._getJSON('/v2/catalogs/default/healthcheck')

  def executeBGHeartbeat(self):
    """Executes a Business Glossary Heartbeat"""
    logging.info('Heartbeat')
    return self._getJSON('/v3/glossary_terms/heartbeat')

  def executeBGHealthCheck(self):
    """Executes a Business Glossary health check"""
    return self._getJSON('/v3/glossary_terms/admin/open-metadata/healthcheck')

  # TODO: Returning a 404
  def executeTenantInitStatusCheck(self):
    """Executes a Tenant init status check"""
    return self._getJSON('/v3/glossary_status/tenant_init_status')

  def getVersionId(self, artifact_id):
    """Returning the Version of an artifact"""
    resJSON = self.search(f'entity.artifacts.artifact_id:{artifact_id}')
    return resJSON['rows'][0]['entity']['artifacts']['version_id']

  def _loadPayload(self, payloadFile):
    """Loading JSON Payload from a file"""
    jsonPath = os.path.join(self.payloadsPath, payloadFile)
    logging.info(f'Loading Payload: {jsonPath}')
    with open(jsonPath, 'r') as f:
      return json.load(f)

    def _postFile(self, endpoint, files, contentType='application/octet-stream', statusCheck=202):
    """POST requests that use a zip file payload, but return nothing"""
    res = self._createRequest(self.session.post, endpoint, contentType, statusCheck, files=files)
    logging.info(res.text)
