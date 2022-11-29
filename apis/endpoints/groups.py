from utilities import csvProcessing, subAPIs


class GroupsAPI(subAPIs.SubAPI):
  """This class represents all functions related to users"""

  # GET functions
  def getAllGroups(self):
    """Get all roles"""
    return self.mainAPI._getJSON('/usermgmt/v2/groups')

   # POST functions
  def addGroup(self, payload):
    """Add a new group to the system"""
    print(payload)
    return self.mainAPI._POST('/usermgmt/v2/groups', payload, 'application/json', 201)

  def getGroupMembers(self, group_id):
    """get all memebrs of a group """
    return self.mainAPI._getJSON('/usermgmt/v2/groups/'+group_id+'/members')

  def addMemberToGroup(self, group_id, payload):
    """add memeber to group"""
    return self.mainAPI._POST('/usermgmt/v2/groups/'+group_id+'/members', payload)
  