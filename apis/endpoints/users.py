import ast
from utilities import csvProcessing, subAPIs
import csv
import logging

class UsersAPI(subAPIs.SubAPI):
  """This class represents all functions related to users"""

  # GET functions
  def getAllUsers(self):
    """Get all users"""
    return self.mainAPI._getJSON('/icp4d-api/v1/users')

  def getUser(self, user_name):
    """Get information about a given user"""
    return self.mainAPI._getJSON(f'/icp4d-api/v1/users/{user_name}')

  def getUserIdByName(self, user_name):
    """Get the id for a given user"""
    return self.mainAPI._getJSON(f'/icp4d-api/v1/users/{user_name}')["UserInfo"]["uid"]

  # Get all user of a given role
  def getRoleByName(self, roleName):
    """Get all users that have a given role"""
    resJSON = self.mainAPI._getJSON('/icp4d-api/v1/roles')
    role = [obj for obj in resJSON['Roles'] if(obj['role_name'] == roleName)]
    try:
      return role[0]['id']
    except:
      raise ValueError('No Role found')

  # POST functions
  def addUser(self, payload):
    """Add a new user to the system"""
    return self.mainAPI._POST('/icp4d-api/v1/users', payload)

  # Functions for mass user update
  def _getUserPayload(self, userRow, user_roles):
    return {
      'user_name': userRow['username'],
      'password': userRow['password'],
      'displayName': userRow['displayName'],
      'user_roles': user_roles,
      'email': userRow['email']
    }

  def _updateUserFromRow(self, userRow):
    user_roles = ast.literal_eval(userRow['user_roles'])
    payload = self._getUserPayload(userRow, user_roles)
    self.addUser(payload)

  def updateUsersFromTable(self, userTable):
    for _, userRow in userTable.iterrows():
        self._updateUserFromRow(userRow)

  def _addUser2Table(self, table, userJSON):
    logging.debug(userJSON)
    row = self._creatUsersRow(userJSON)
    return table.append(row, ignore_index=True)

  def _creatUsersRow(self, user):
    logging.debug("user")
    logging.debug(user)
    return {
      'displayName': user["displayName"],
      'email': user["email"],
      'username': user["username"],
      'uid': user["uid"],
      'user_roles': user["user_roles"],
      'permissions': user["permissions"]
    }

  def users2Table(self, usersJSON):
    """creates a table from a list of users
    Args:
        usersJSON (dict): JSON formatted output of the WKC API for a list of users
    Returns:
      pandas.DataFrame: table of users
    """
    usersFound = len(usersJSON['UsersInfo'])
    assert usersFound > 0, 'No Users found'
    return csvProcessing.items2Table(self._addUser2Table, usersJSON['UsersInfo'])

  def users2CSV(self, usersJSON, filePath):
    """creates a csv file of users
    Args:
        usersJSON (dict): JSON formatted output of the WKC API for a list of users
        filePath (str): name or filepath for the creation of the csv file
    """
    csvProcessing.items2CSV(self._addUser2Table, usersJSON['UsersInfo'], filePath)
