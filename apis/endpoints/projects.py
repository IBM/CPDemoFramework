from utilities import subAPIs
import logging

class ProjectsAPI(subAPIs.SubAPI):
  """This class represents all functions related to projects"""

  # GET functions
  def getListOfProjects(self):
    """Get a list of projects"""
    return self.mainAPI._getJSON('/v2/projects')
