from utilities import csvProcessing, subAPIs


class GroupsAPI(subAPIs.SubAPI):
  """This class represents all functions related to users"""

  # GET functions
  def getAllGroups(self):
    """Get all roles"""
    return self.mainAPI._getJSON('/usermgmt/v2/groups')

  