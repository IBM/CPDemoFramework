import json
import requests
from requests.packages import urllib3

def getAPIKey(cpdURL, cpdUserName, cpdPassword):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    signin_url = f'{cpdURL}/v1/preauth/signin'
    credentials = {"username": cpdUserName, "password": cpdPassword}
    headers =  {'Content-Type': 'application/json;charset=UTF-8'}
    response = requests.post(signin_url, data=json.dumps(credentials), headers=headers, verify=False)
    resJSON = response.json()
    apikey_url = f'{cpdURL}/usermgmt/v1/user/apiKey'
    access_token = resJSON['token']
    headers['Authorization'] = f'Bearer {access_token}'
    response = requests.get(apikey_url, headers=headers, verify=False)
    output = response.json()
    print(output)
    return output["apiKey"]