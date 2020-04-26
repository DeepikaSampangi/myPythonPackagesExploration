import json
import requests



get_req = requests.get('https://google.com')

#######

get_req_params = {"key1":"value1", "key2":"value2"}
get_req_params = requests.get("<url>", params=get_req_params)

get_req_with_auth = requests.get('<url>', auth=('username', 'password'))

#######

# content is a raw string format
print("Type of content : ", type(get_req.content))

#text is a unicode encoding of the content
print("Type of text : ", type(get_req.text))

# Encoding value of a request
print(get_req.encoding)

#########

payload = {'key':'value'}
url = '<url>'
headers = {'Content-Type': 'application/json'}
post_req_headers = requests.post(url = url, headers=headers, data=json.dumps(payload))