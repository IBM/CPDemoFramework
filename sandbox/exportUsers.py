import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import pandas
import sys
sys.path.append('../')
import apis
userApi = apis.endpoints.UsersAPI()

usersJSON = userApi.getAllUsers()
userApi.users2CSV(usersJSON, sys.argv[1])
usersTable = pandas.read_csv(sys.argv[1])        
usersTable
print("success")
