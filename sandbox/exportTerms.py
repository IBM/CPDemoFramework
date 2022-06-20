import logging
import pandas

logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append('../')
from apis import endpoints, MainAPI, usecases

categoriesAPI = endpoints.CategoriesAPI()
termsAPI = endpoints.TermsAPI()
mainAPI = MainAPI()
refDataAPI = endpoints.RefDataAPI(mainAPI)
# Get list of terms 
termsJSON = mainAPI.search(f'metadata.artifact_type:glossary_term')
termsAPI.terms2CSV(termsJSON, sys.argv[1])