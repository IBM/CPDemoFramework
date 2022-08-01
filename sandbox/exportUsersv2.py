import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import pandas
import sys
sys.path.append('../')
import apis
import os
from decouple import config

userApi = apis.endpoints.UsersAPI()

CPD_USER_NAME =  config('WKCUSER')
CPD_USER_PASSWORD =  config('PASSWORD')
CPD_URL = "https://"+config('TZHOSTNAME')
CPD_API_KEY = config('APIKEY')

os.system('cpd-cli config users set sandbox-profile --username'+ CPD_USER_NAME + '--apikey'+ CPD_API_KEY)
os.system('cpd-cli config profiles set sandbox-profile --username'+ CPD_USER_NAME + '--url'+ CPD_URL)

data = os.popen("cpd-cli service-instance list --profile sandbox-profile").read()
print(data)
usersJSON = userApi.getAllUsers()

for user in usersJSON["UsersInfo"] :
    if "email" not in user:
        user["email"] = '--'

userApi.users2CSV(usersJSON, sys.argv[1])
usersTable = pandas.read_csv(sys.argv[1])        
usersTable
