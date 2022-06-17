import logging
import pandas

logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append('../..')
from apis import endpoints, MainAPI, usecases

categoriesAPI = endpoints.CategoriesAPI()
termsAPI = endpoints.TermsAPI()
mainAPI = MainAPI()
refDataAPI = endpoints.RefDataAPI(mainAPI)
# Bring categories back to object for bulk updates to catalog
categoriesTable = pandas.read_csv('export_categories.csv')        
categoriesAPI.updateCategoriesFromTable(categoriesTable)
