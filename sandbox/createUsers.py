import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append('../')
import os
from decouple import config
import pandas
import ast
import cpdCLIUtils

CPD_USER_NAME =  config('WKCUSER')
CPD_USER_PASSWORD =  config('PASSWORD')
CPD_URL = "https://"+config('TZHOSTNAME')
cpdAPIKey = cpdCLIUtils.getAPIKey(CPD_URL, CPD_USER_NAME, CPD_USER_PASSWORD)

"""
userTableDeafult = pandas.read_csv(sys.argv[1])
if "password" not in userTableDeafult.columns:
    usersTable = pandas.DataFrame(columns=['username','password','email','displayName','user_roles'])
    password = input("Please enter a password:\n")
    for i in range(len(userTableDeafult)):
        usersTable.loc[len(usersTable.index)] = [userTableDeafult.loc[i,'username'],CPD_USER_PASSWORD if userTableDeafult.loc[i,'username']==CPD_USER_NAME else password,userTableDeafult.loc[i,'email'],userTableDeafult.loc[i,'displayName'],";".join(ast.literal_eval(userTableDeafult.loc[i,'user_roles']))] 
usersTable.to_csv(sys.argv[1],index=False)
"""
os.system('cpd-cli config users set '+ CPD_USER_NAME +' --username '+ CPD_USER_NAME + ' --apikey '+ cpdAPIKey)

os.system('cpd-cli config profiles set sandbox-profile --user '+ CPD_USER_NAME + ' --url '+ CPD_URL)

data = os.popen('cpd-cli user-mgmt bulk-upsert-users --from-csv-file '+ sys.argv[1] +' --profile sandbox-profile').read()
print(data)
print("success")
