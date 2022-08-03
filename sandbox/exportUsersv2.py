import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import pandas
import sys
sys.path.append('../')
import os
from decouple import config
import json

CPD_USER_NAME =  config('WKCUSER')
CPD_USER_PASSWORD =  config('PASSWORD')
CPD_URL = "https://"+config('TZHOSTNAME')
CPD_API_KEY = config('APIKEY')
os.system('cpd-cli config users set '+ CPD_USER_NAME +' --username '+ CPD_USER_NAME + ' --apikey '+ CPD_API_KEY)

os.system('cpd-cli config profiles set sandbox-profile --user '+ CPD_USER_NAME + ' --url '+ CPD_URL)
usersJSON = json.loads(os.popen("cpd-cli user-mgmt list-users --profile sandbox-profile --output json  ").read())
print(usersJSON)


for user in usersJSON:
    if "email" not in user:
        user["email"] = '--'

     
usersTable = pandas.DataFrame(columns=['displayName','email','permissions','uid','user_roles','username'])

for user in usersJSON:
    usersTable.loc[len(usersTable.index)] = [user['displayName'],user['email'],user['permissions'],user['uid'],user['user_roles'],user['username']] 
print(usersTable)
usersTable.to_csv(sys.argv[1],index=False)