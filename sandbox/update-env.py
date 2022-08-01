import sys

hostname = sys.argv[1]
wkcuser=sys.argv[2]
password=sys.argv[3]
try:
    api_key = sys.argv[4]
except:
    api_key = "demo_api_key"

f = open("../.env", "w")
f.write("TZHOSTNAME="+hostname+"\nWKCUSER="+wkcuser+"\nPASSWORD="+password+"\nAPIKEY="+api_key)
f.close()