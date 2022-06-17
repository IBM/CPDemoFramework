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
termTable = pandas.read_csv('export_terms.csv')        
termsAPI.updateTermsFromTable(termTable)