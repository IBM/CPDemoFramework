from utilities import subAPIs

class JobsAPI(subAPIs.SubAPI):
  """This class represents all functions related to jobs"""

  # GET functions
  def getListOfJobs(self, project_id):
    """Get a list of jobs for a given project"""
    return self.mainAPI._getJSON(f'/v2/jobs/?project_id={project_id}')

  # GET functions
  def getListOfJobRuns(self, project_id, job_id):
    """Get a list of jobs for a given project"""
    return self.mainAPI._getJSON(f'/v2/jobs/{job_id}/runs?project_id={project_id}')

  def getRunOfAJob(self, job_id, run_id, project_id):
    """Get the results of a run from a given job in a given project"""
    return self.mainAPI._getJSON(f'/v2/jobs/{job_id}/runs/{run_id}?project_id={project_id}')

  def getLogOfAJobRun(self, job_id, run_id):
    """Get the log of a given job and a given run"""
    return self.mainAPI._getJSON(f'/v2/jobs/{job_id}/runs/{run_id}/logs')

  # POST functions
  def startJobRun(self, job_id, project_id, payloadFile='jobs/startJobRun.json'):
    """Start a given job in a given project"""
    payload = self.mainAPI._loadPayload(payloadFile)
    return self.mainAPI._POST(f'/v2/jobs/{job_id}/runs?project_id={project_id}', payload, statusCheck=201)

  # DELETE functions
  def deleteRunOfAJob(self, job_id, run_id, project_id):
    """Delete the log of a given run of a job in a given project"""
    return self.mainAPI._DELETE(f'/v2/jobs/{job_id}/runs/{run_id}?project_id={project_id}', statusCheck=204)
