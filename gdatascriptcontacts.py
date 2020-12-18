import gdata
import gdata.gauth
import gdata.contacts.client
import json
import requests
import apiclient
import httplib2
from oauth2client import _helpers
from oauth2client import _pkce
from oauth2client import clientsecrets
from oauth2client import transport
from oauth2client import client

GOOGLE_CLIENT_ID = '81802460251-example.apps.googleusercontent.com' # -example - not real Provided in the APIs console
GOOGLE_CLIENT_SECRET = '18WgKRPSwdjjsawbOVgAXzcZNrOW-W3' # -example - not real secret  Provided in the APIs console
GOOGLE_TOKEN_URI = 'https://oauth2.googleapis.com/token'
GOOGLE_REVOKE_URI = 'https://oauth2.googleapis.com/revoke'
ACCESS_TOKEN = ''
REFRESH_TOKEN = '1//04KSv5y8sd76fsdf678sdRAAGAQSNwF-L9skljhnf9djs8dsd87s3j8orMhcg28bB4btGqC1ePKXQlxA3shSM0M2GyFMoFtj6RoHmQ'

resp=''
ident=''
telnum=''
name=''
surname=''
title=''
pager=''
gecos=''
mail=''
mobile=''
rel=''
res=[]

credentials = client.OAuth2Credentials(
    access_token=None,  # set access_token to None since we use a refresh token
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    refresh_token=REFRESH_TOKEN,
    token_expiry=None,
    token_uri=GOOGLE_TOKEN_URI,
    user_agent=None,
    revoke_uri=GOOGLE_REVOKE_URI)
credentials.refresh(httplib2.Http())  # refresh the access token (optional)
resp=json.loads(credentials.to_json())
resp=resp['access_token']

#print (resp)
http = credentials.authorize(httplib2.Http())  # apply the credentials
access_token = resp
#JSON with access token
r=requests.get('https://www.google.com/m8/feeds/contacts/default/full?&access_token=%s&alt=json&v=3.0&max-results=1000&start-index=0&group=https://www.google.com/m8/feeds/groups/example@gmail.com/base/4271963ndz335e4d2' % access_token) 
# 4271963ndz335e4d2 - example - google contacts groupID - label
data= json.loads(r.text);
#id
#data=data['feed']['entry'][0]['id']['$t']
#title
#data=data['feed']['entry'][0]['title']['$t']
#telephone number
#data=data['feed']['entry'][0]['gd$phoneNumber'][0]['$t']
#Name
#data=data['feed']['entry'][0]['gd$name']['gd$givenName']['$t']
#Surname
#data=data['feed']['entry'][1]['gd$name']['gd$familyName']['$t']

for test in data['feed']['entry']:
    ident=test['id']['$t']
    res=ident.rsplit('/',1)
    ident=res[1]
    print (ident)
    title=test['title']['$t']
    print (title)
    rel=test['gd$phoneNumber'][0]['rel']
    print (rel)
    telnum=test['gd$phoneNumber'][0]['$t']
    print (telnum)
    name=test['gd$name']['gd$givenName']['$t']
    print (name)
    surname=test['gd$name']['gd$familyName']['$t']
    print (surname)
    
#print (data)

