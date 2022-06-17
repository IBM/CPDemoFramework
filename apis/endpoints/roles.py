import ast
from utilities import csvProcessing, subAPIs
import csv
import logging

class RolesAPI(subAPIs.SubAPI):
  """This class represents all functions related to users"""

  # GET functions
  def getAllRoles(self):
    """Get all roles"""
    return self.mainAPI._getJSON('/api/v1/usermgmt/v1/roles')

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
  def addRole(self, payload):
    """Add a new role to the system"""
    return self.mainAPI._POST('/api/v1/usermgmt/v1/roles', payload)

  # Functions for mass user update
  def _getRolePayload(self, roleRow, permissions):
    return {
      'role_name': roleRow['role_name'],
      'description': roleRow['description'],
      'permissions': permissions
    }

  def _updateRoleFromRow(self, roleRow):
    permissions = ast.literal_eval(roleRow['permissions'])
    payload = self._getRolePayload(roleRow, permissions)
    self.addRole(payload)

  def updateRolesFromTable(self, roleTable):
    for _, roleRow in roleTable.iterrows():
        self._updateRoleFromRow(roleRow)

  def _addRole2Table(self, table, roleJSON):
    logging.debug(roleJSON)
    row = self._creatRoleRow(roleJSON)
    return table.append(row, ignore_index=True)

  def _creatRoleRow(self, role):
    logging.debug("role")
    logging.debug(role)
    return {
      'role_name': role['role_name'],
      'description': role['description'],
      'permissions': role['permissions']
    }

  def roles2Table(self, rolesJSON):
    """creates a table from a list of roles
    Args:
        usersJSON (dict): JSON formatted output of the WKC API for a list of roles
    Returns:
      pandas.DataFrame: table of roles
    """
    usersFound = len(rolesJSON['UsersInfo'])
    assert usersFound > 0, 'No Users found'
    return csvProcessing.items2Table(self._addRole2Table, rolesJSON['UsersInfo'])

  def roles2CSV(self, rolesJSON, filePath):
    """creates a csv file of roles
    Args:
        rolesJSON (dict): JSON formatted output of the WKC API for a list of roles
        filePath (str): name or filepath for the creation of the csv file
    """
    csvProcessing.items2CSV(self._addRole2Table, rolesJSON['UsersInfo'], filePath)
