import apis
import filecmp
import os
import time
import unittest

class RefDataAPI(unittest.TestCase):
  @classmethod
  def setUpClass(cls):  # prepare something ahead of all tests
    cls.api = apis.endpoints.RefDataAPI()
    cls.testString = 'T3st'
    cls.uploadFilename = 'tests/csvs/refDataUpload.csv'
    cls.downloadFilename = 'tests/csvs/refDataDownload.csv'

  def test_refData(self):
    res = self.api.getListOfRefData(self.testString)
    assert res['size'] == 0, f'reference Dataset with name {self.testString} already exists, please delete or rename it manually'

    self.api.createRefData('../tests/payloads/reference_data/createRefData.json')

    time.sleep(1)  # necessary to wait here for ref data to be found by getListOfRefData
    res = self.api.getListOfRefData(self.testString)
    assert res['size'] == 1
    artifact_id = res['rows'][0]['artifact_id']
    version_id = res['rows'][0]['entity']['artifacts']['version_id']

    self.api.getRefData(artifact_id, version_id)

    self.api.loadRefDataFromCSV(artifact_id, self.uploadFilename, version_id)

    self.api.getRefDataCSV(artifact_id, self.downloadFilename, version_id)
    assert filecmp.cmp(self.uploadFilename, self.downloadFilename)
    os.remove(self.downloadFilename)

    self.api.deleteRefData(artifact_id)
