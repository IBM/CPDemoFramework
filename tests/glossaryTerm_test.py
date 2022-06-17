from apis import endpoints, MainAPI
import filecmp
import os
import time
import unittest

class TermsAPI(unittest.TestCase):
  @classmethod
  def setUpClass(cls):  # prepare something ahead of all tests
    cls.mainAPI = MainAPI()
    cls.t_api = endpoints.TermsAPI(cls.mainAPI)
    cls.w_api = endpoints.WorkflowsAPI(cls.mainAPI)
    cls.testString = 'T3st'

  def test_TermsWithWorkflow(self):
    res = self.mainAPI.search('T3st')
    assert res['size'] == 0, f'Term with name {self.testString} already exists, please delete or rename it manually'

    newTerm = self.t_api.createTerm('glossary_terms/createTerm.json', False)["resources"]
    assert len(newTerm) == 1

    artifact_id = newTerm[0]['artifact_id']
    version_id = newTerm[0]['version_id']

    termJSON = self.t_api.getDraftVersionsOfTerm(artifact_id)
    assert termJSON["count"] == 1
    #termJSON = t_api.getPublishedVersionsOfTerm(artifact_id)

    res = self.w_api.getWorkflowUserTaskByArtifact(artifact_id, version_id)["resources"]
    assert len(res) == 1
    # res["resources"][0]["entity"]["form_properties"]

    taskId = res[0]["metadata"]["task_id"]
    self.w_api.updateWorkflowUserTask(taskId, 'workflows/publishTask.json')

    pubTerm = self.t_api.getPublishedVersionsOfTerm(artifact_id)["resources"]
    assert len(pubTerm) == 1

    artifact_id = pubTerm[0]["metadata"]['artifact_id']
    version_id = pubTerm[0]["metadata"]['version_id']

    delTerm = self.t_api.deleteTerm(artifact_id, version_id, False)["resources"]
    assert len(delTerm) == 1

    artifact_id = delTerm[0]['artifact_id']
    version_id = delTerm[0]['version_id']

    res = self.w_api.getWorkflowUserTaskByArtifact(artifact_id, version_id)["resources"]
    assert len(res) == 1
    # res["resources"][0]["entity"]["form_properties"]

    taskId = res[0]["metadata"]["task_id"]
    self.w_api.updateWorkflowUserTask(taskId, 'workflows/deleteTask.json')

    time.sleep(1)  # necessary to wait here for ref data to be found by getListOfRefData

    res = self.mainAPI.search('T3st')
    assert res['size'] == 0, f'Term with name {self.testString} still exists, please delete or rename it manually'

  def test_TermsWithoutWorkflow(self):
    res = self.mainAPI.search('T3st')
    assert res['size'] == 0, f'Term with name {self.testString} already exists, please delete or rename it manually'

    newTerm = self.t_api.createTerm('glossary_terms/createTerm.json', True)["resources"]
    assert len(newTerm) == 1

    artifact_id = newTerm[0]['artifact_id']
    version_id = newTerm[0]['version_id']

    pubTerm = self.t_api.getPublishedVersionsOfTerm(artifact_id)["resources"]
    assert len(pubTerm) == 1

    artifact_id = pubTerm[0]["metadata"]['artifact_id']
    version_id = pubTerm[0]["metadata"]['version_id']

    delTerm = self.t_api.deleteTerm(artifact_id, version_id, True)

    time.sleep(1)  # necessary to wait here for ref data to be found by getListOfRefData

    res = self.mainAPI.search('T3st')
    assert res['size'] == 0, f'Term with name {self.testString} still exists, please delete or rename it manually'
