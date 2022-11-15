
import logging
import pandas

logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append('../')
from apis import endpoints, MainAPI, usecases
mainAPI = MainAPI()
rulesAPI = endpoints.RulesAPI(mainAPI)
rulesAPI.exportDataProtectionRules(sys.argv[1])
print("success")