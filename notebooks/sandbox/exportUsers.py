import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import pandas
import sys
sys.path.append('../..')
import apis
userApi = apis.endpoints.UsersAPI()

usersJSON = userApi.getAllUsers()
userApi.users2CSV(usersJSON, 'users_export.csv')
usersTable = pandas.read_csv('users_export.csv')        
usersTable
