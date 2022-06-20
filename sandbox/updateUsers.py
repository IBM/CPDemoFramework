import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import pandas
import sys
sys.path.append('../')
import apis
userApi = apis.endpoints.UsersAPI()

usersTable = pandas.read_csv(sys.argv[1])        
userApi.updateUsersFromTable(usersTable)
