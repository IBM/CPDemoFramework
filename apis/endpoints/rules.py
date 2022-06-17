from utilities import subAPIs

class RulesAPI(subAPIs.SubAPI):
  """This class represents all functions related to data protection rules"""

  # GET functions
  def getListOfRules(self):
    """Get a list of rules"""
    return self.mainAPI._getJSON('/v3/enforcement/rules')

  # DELETE functions
  def deleteRule(self, rule_id):
    """Delete the log of a given rule"""
    return self.mainAPI._DELETE(f'/v3/enforcement/rules/{rule_id}', statusCheck=204)
