import http.client
import urllib

key = "54CDA6FJF4RCJ92C"
cmail = "alexbhend@cmail.carleton.ca"
group = "L2-M-1"
identifier = 'b'

params = urllib.parse.urlencode({'field1':cmail, 'field2':group, 'field3':identifier, 'key':key }) 
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")

conn.request("POST", "/update", params, headers)
response = conn.getresponse()
print (response.status, response.reason)
data = response.read()
conn.close()