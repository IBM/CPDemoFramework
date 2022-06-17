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
# Get list of categories and export to csv
categoriesJSON = mainAPI.search(f'metadata.artifact_type:category')
categoriesAPI.categories2CSV(categoriesJSON,"export_categories.csv")
categoriesTable = pandas.read_csv('export_categories.csv')        
categoriesTable