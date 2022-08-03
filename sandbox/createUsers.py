import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append('../')
import os
from decouple import config


CPD_USER_NAME =  config('WKCUSER')
CPD_USER_PASSWORD =  config('PASSWORD')
CPD_URL = "https://"+config('TZHOSTNAME')
CPD_API_KEY = config('APIKEY')

os.system('cpd-cli config users set '+ CPD_USER_NAME +' --username '+ CPD_USER_NAME + ' --apikey '+ CPD_API_KEY)

os.system('cpd-cli config profiles set sandbox-profile --user '+ CPD_USER_NAME + ' --url '+ CPD_URL)

data = os.popen('cpd-cli user-mgmt bulk-upsert-users --from-csv-file '+ sys.argv[1] +' --profile sandbox-profile').read()
print(data)
#usersTable = pandas.read_csv(sys.argv[1])        
#userApi.updateUsersFromTable(usersTable)
