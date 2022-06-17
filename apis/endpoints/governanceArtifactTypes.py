from utilities import subAPIs

class GovArtifactAPI(subAPIs.SubAPI):
  """This class represents all functions related to governance artifact types"""

  # GET functions
  def getArtefactByType(self, artifact_type):
    """Get the draft artifacts by a given type
    Returns or or many artifacts"""
    return self.mainAPI._getJSON(f'/v3/governance_artifact_types/{artifact_type}')

  def getCustomAttributes(self, artifactType):
    """Get all Custom Attributes for a given artifact type
    Returns many objects in a JSON structure """
    return self.mainAPI._getJSON(f'/v3/governance_artifact_types/{artifactType}/custom_attribute_definitions')

  def getCustomAttributeByName(self, artifactType, name):
    """Get one Custom Attribute for a given artifcat type by its name
    Filters from the list of all custom attributes the one that matches the name provided.
    Returns one or none object"""
    res = self.getCustomAttributes(artifactType)
    customAttribute = list(filter(lambda x: x["metadata"]["name"] == name, res))
    return customAttribute

  def getActivityLogEntries(self, artifact_type, artifact_id, version_id):
    """Get all actvity log entries for a given artifact type
    Returns many objects in a JSON structure """
    return self.mainAPI._getJSON(f'/v3/governance_artifact_types/{artifact_type}/{artifact_id}/versions/{version_id}/aggregated_logs')

  def getActivityLogEntry(self, artifact_type, artifact_id, version_id, mod_id):
    """Get all actvity log entries for a given artifact type
    Returns many objects in a JSON structure """
    return self.mainAPI._getJSON(f'/v3/governance_artifact_types/{artifact_type}/{artifact_id}/versions/{version_id}/aggregated_logs{mod_id}')


  #TODO: Verify functionality
  def exportArtifactsZIP(self, filename, artifact_id_mode="always", artifact_types="all", category_ids="all_top_level"):
    """Export a ZIP file containing artifacts export
    Requires CP4D 4.x"""
    endpoint = f'/v3/governance_artifact_types/export?artifact_id_mode={artifact_id_mode}&artifact_types={artifact_types}&category_ids={category_ids}'
    self.mainAPI._getFile(endpoint, filename)

  # POST functions
  def createCustomAttribute(self, artifact_type, payloadFile='governance_artifact_types/createCustomAttribute.json'):
    """Create a Custom Attribute for a given artifact type from a payload file provided"""
    payload = self.mainAPI._loadPayload(payloadFile)
    return self.mainAPI._POST(f'/v3/governance_artifact_types/{artifact_type}/custom_attribute_definitions', payload, statusCheck=201)

  #TODO: create a _postFile function
  def importArtifactsZIP(self, filename):
    """Import artifacts from a zip file
    Requires CP4D 4.x"""
    files = {'file': (filename, open(filename, 'rb'), 'application/x-zip-compressed')}
    endpoint = f'/v3/governance_artifact_types/import'
    self.mainAPI._putFile(endpoint, files=files, contentType='multipart/form-data', statusCheck=202)

  # DELETE functions
  def deleteCustomAttribute(self, artifact_type, custom_attribute_definition_id):
    """Delete a Custom Attribute of a given artifact type"""
    return self.mainAPI._DELETE(f'/v3/governance_artifact_types/{artifact_type}/custom_attribute_definitions/{custom_attribute_definition_id}', statusCheck=200)
