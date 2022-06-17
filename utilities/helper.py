"""Helper Functions for the WKC API"""
import inspect
import logging
from os.path import dirname

def getPayloadsPath():
  """Returns the path of the payloads directory. To be precise, it returns ../payloads
  Returns:
      str: path to the payload directory
  """
  repoPath = dirname(dirname(__file__))
  payloadsPath = f'{repoPath}/payloads'
  logging.debug(f'Payloads Path: {payloadsPath}')
  return payloadsPath

def _getFunctionName(positionOnStack):
  """gets function name when given the position in the function stack when called
  Args:
      positionOnStack (int): refers to the location in the stack, i.e. the nth most recently called function
  Returns:
      str: function name
  """
  return inspect.stack()[positionOnStack][3]  # second index refers to the position of the functions name in the stack entry

def getRequestName():
  """gets HTTP request type when called in main._logAPIFunctionInfo. To be precise, it returns the name of an functions without the first character of the 4th function on the function stack
  Returns:
      str: requestName
  """
  functionName = _getFunctionName(4)
  return functionName[1:]  # strip '_'

def sendRequestWithPayload(requestFun, url, headers, payload, files):
  """Sends a request, can optionally be enriched with payload, headers and files.
  Args:
      requestFun (function): HTTP request function from apis.MainAPI
      url (str): full URL with endpoint for the HTTP request
      headers (dict): JSON formatted headers. Can be None
      payload (dict): JSON formatted request payload. Can be None
      files (dict): JSON formatted files used for the request. Can be None
  Returns:
      requests.Response: HTTP response of the request
  """
  if payload:
    logging.debug('adding json')
    return requestFun(url, headers=headers, json=payload, verify=False)
  elif files:
    return requestFun(url, headers=headers, files=files, verify=False)
  else:
    return requestFun(url, headers=headers, verify=False)
