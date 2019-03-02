import requests
import base64
import pprint
import json
from bs4 import BeautifulSoup

#website to scrape ticket prices from
#URL is a string
#consumer key: consumer secret key
#def createAuthorizationToken(username,password,consumerKey,consumerSecret):
#userKey = consumerKey + ":" + consumerSecret
userKey = "fsKOaomCzX2hmEqH0I4AAlLiNooPwPK9:gO3swKOt9Wk8FCnd"
authToken = "Basic " + base64.b64encode(bytes(userKey, "utf-8")).decode()

##POST parameters to generate a access token
headers = {
    'Content-Type': 'application/json',
    'Authorization': authToken,
}

login = dict(grant_type='client_credentials',
             username='ticketandfestivallovers@gmail.com',
             password='GeauxTigers01',
             scope='PRODUCTION')
##Make the api call
url = 'https://api.stubhub.com/login'
response = requests.post(url, headers =headers, data = login)
print(response)
#response = requests.post('https://api.stubhub.com/sellers/oauth/accesstoken?grant_type=client_credentials', headers=header, data=data)
