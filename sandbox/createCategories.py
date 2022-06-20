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
# Create new categories from file
categoriesTable = pandas.read_csv(sys.argv[1])        
for index, row in categoriesTable.iterrows():
    categoriesAPI.createCategory(row['name'], row['short_description'], row['long_description'])