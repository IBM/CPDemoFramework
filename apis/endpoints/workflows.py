from utilities import subAPIs

class WorkflowsAPI(subAPIs.SubAPI):
  """This class represents all functions related to workflows"""

  # GET functions
  def getAllWorkflows(self):
    """Get all Workflows
    Returns JSON structure"""
    return self.mainAPI._getJSON('/v3/workflows')

  def getWorkflowById(self, workflow_id):
    """Get a given workflow"""
    return self.mainAPI._getJSON(f'/v3/workflows/{workflow_id}')

  def getWorkflowUserTasks(self):
    """Get all workflows tasks
    Returns JSON structure
    TaskIds can be queried as this: ['resources'][0]['metadata']['task_id']"""
    return self.mainAPI._getJSON(f'/v3/workflow_user_tasks')

  def getWorkflowUserTaskById(self, task_id):
    """Get a workflow tasks by a given id
    Returns a JSON structure
    Contains the possible actions in the "form_properties" object.
    That holds enum_values and the id specifies the possible action"""
    return self.mainAPI._getJSON(f'/v3/workflow_user_tasks/{task_id}')

  def getWorkflowUserTaskByArtifact(self, artifact_id, version_id):
    """Get a workflow task related to a specific artifact"""
    return self.mainAPI._getJSON(f'/v3/workflow_user_tasks?artifact_id={artifact_id}&version_id={version_id}')

  def getWorkflowHousekeeping(self):
    """you can query for workflows in an inconsistent state using the following call
    Be aware that you need to “page” through all currently running workflow instances by repeatedly running the above statement and increasing the offset by 100 each time. The paging is necessary to prevent timeouts. The resources listed in the response show the inconsistencies found.
    Also be aware that the total_count reported by the housekeeping endpoint refers to the number of inconsistencies found. However, the limit and offset input parameters refer to the currently active workflow instances.
    See https://www.ibm.com/support/pages/node/6479631"""
    return self.mainAPI._getJSON(f'/v3/workflows/housekeeping?limit=100&offset=0')


  # POST functions
  def queryAllWorkflows(self, payloadFile='workflows/queryAllWorkflows.json'):
    """Get contents of all workflows"""
    payload = self.mainAPI._loadPayload(payloadFile)
    return self.mainAPI._POST('/v3/workflows/all/query', payload)

  def updateWorkflowUserTask(self, task_id, payloadFile='workflows/updateWorkflowUserTask.json'):
    """Update a given workflow task by a payload provided"""
    payload = self.mainAPI._loadPayload(payloadFile)
    return self.mainAPI._POST(f'/v3/workflow_user_tasks/{task_id}/actions', payload, statusCheck=204)

  def doWorkflowHousekeeping(self):
    """For each "page" that contains an inconsistent workflow you can remove those inconsistent workflows on that page using this call:
    Be aware that in case an inconsistent workflow has more than 10 artifacts attached you need to repeatedly invoke the cleanup using above command because on each invocation only 10 artifacts are cleaned up. You need to repeat this until all artifacts managed by the inconsistent workflow have been processed.
    See https://www.ibm.com/support/pages/node/6479631"""
    return self.mainAPI._POST(f'/v3/workflows/housekeeping?limit=100&offset=0')
