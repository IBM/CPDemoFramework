import json
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

  def exportDataProtectionRules(self, file_name):
    return self.mainAPI._getFile('/v3/enforcement/rules/export',file_name ,200)
  
  def importDataProtectionRules(self, dataprotectionrulefile):
    payload = json.load(open(dataprotectionrulefile, encoding= 'utf-8' ))
    expected = [element for element in payload["rules"] if element['governance_type_id'] != "ResourceControl" ]
    payload["rules"]=expected
    return self.mainAPI._POST('/v3/enforcement/rules/import',payload,'application/octet-stream',200) 
