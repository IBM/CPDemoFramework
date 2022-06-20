import sys

hostname = sys.argv[1]
wkcuser=sys.argv[2]
password=sys.argv[3]

f = open("../.env", "w")
f.write("TZHOSTNAME="+hostname+"\nWKCUSER="+wkcuser+"\nPASSWORD="+password)
f.close()