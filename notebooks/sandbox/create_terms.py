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
# Create new terms from file
termsTable = pandas.read_csv('new_terms.csv')    
for index, row in termsTable.iterrows():
    termAbbreviations = [row['name'][0:2]]
    termsAPI.createTerm(termAbbreviations, row['name'], row['short_description'], row['long_description'])