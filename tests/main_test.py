import apis
from requests.packages import urllib3
import unittest

class MainAPI(unittest.TestCase):
  @classmethod
  def setUpClass(cls):  # prepare something ahead of all tests
    cls.api = apis.MainAPI()
    cls.testString = 'T3st'
    cls.uploadFilename = 'tests/csvs/refDataUpload.csv'
    cls.downloadFilename = 'tests/csvs/refDataDownload.csv'

  def setUp(self):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

  def test_executeCAMSHealthCheck(self):
    self.api.executeCAMSHealthCheck()

  def test_executeBGHeartbeat(self):
    self.api.executeBGHeartbeat()

  def test_executeBGHealthCheck(self):
    self.api.executeBGHealthCheck()

  def test_executeTenantInitStatusCheck(self):
    self.api.executeTenantInitStatusCheck()
