import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import pandas
import sys
sys.path.append('../')
import apis
import os
userApi = apis.endpoints.UsersAPI()

os.system('cpd-cli user-mgmt bulk-upsert-users --from-csv-file'+ sys.argv[1]+'--profile sandbox-profile')
#usersTable = pandas.read_csv(sys.argv[1])        
#userApi.updateUsersFromTable(usersTable)
