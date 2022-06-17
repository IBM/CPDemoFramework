import apis
from utilities import subAPIs

class CategoryTreeAPI(subAPIs.SubAPI):
  """This class represents all functions related to category tree operations"""
  def __init__(self, mainAPI=None):
    super().__init__(mainAPI)
    self.categoryAPI = apis.endpoints.CategoriesAPI(self.mainAPI)

  def deleteCategoryTree(self, guid):
    """Deletes all categories starting with the provided guid.
    The function iterates over all subcategories and deletes each"""
    res = self.categoryAPI.getListOfCategoriesForParentById(guid)
    if res["size"] > 0:
        for cat in res["rows"]:
            catId = cat["artifact_id"]
            self.deleteCategoryTree(catId)
    # Invoke deletion of category
    self.categoryAPI.deleteCategory(guid)

  def selectTermsCategoryTree(self, guid, termsJSON=None):
    """Extract all Business Terms from a given Category recursivly.
    The function iterates over all subcategories and extract the Terms"""
    if termsJSON is None:
        termsJSON = []
    res = self.categoryAPI.getListOfCategoriesForParentById(guid)
    if res["size"] > 0:
        for cat in res["rows"]:
            catId = cat["artifact_id"]
            self.selectTermsCategoryTree(catId, termsJSON)
        # select all the stuff
    termsJSON.append(self.mainAPI.search(f'categories.primary_category_id:{guid} AND metadata.artifact_type:glossary_term'))
    return termsJSON
