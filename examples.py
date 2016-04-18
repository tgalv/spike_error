import json

import requests


print("Health Check...")
r = requests.get('http://0.0.0.0:5000')
print(r.text, r.status_code)
print 

print("500...")
r = requests.get('http://0.0.0.0:5000/div_zero')
print(r.text[:100], r.status_code)
print 

print("404...")
r = requests.get('http://0.0.0.0:5000/foo')
print (r.text[:100], r.status_code)
print 

print("Happy Path Post...")
r = requests.post('http://0.0.0.0:5000/json_post',
                  data=json.dumps({"name" : "Eggs", "price" : 34.99}), 
                  headers={'Content-Type': 'application/json'})
print(r.text[:100], r.status_code)
print 

print("415...")
r = requests.post('http://0.0.0.0:5000/json_post',
                  data='<say>Hello</say>',
                  headers={'Content-Type': 'application/xml'})
print(r.text[:100], r.status_code)
print 

print("406...")
r = requests.post('http://0.0.0.0:5000/json_post',
                  data=json.dumps({"name" : "Eggs", "price" : 34.99}), 
                  headers={'Content-Type': 'application/json',
                           'Accept': 'text/xml'})
print(r.text[:100], r.status_code)
print 


print("400 Bad Schema...")
r = requests.post('http://0.0.0.0:5000/json_post',
                  data=json.dumps({"name" : 111, "price" : "222"}), 
                  headers={'Content-Type': 'application/json'})
print(r.text[:100], r.status_code)
print 




