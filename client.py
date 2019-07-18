import requests
import json

###Listing tasks(GET METHOD)###
base_url="http://127.0.0.1:5000"
response=requests.get(base_url+"/tasks")
print "###List tasks result###"
print "response status code:",response.status_code,"\n" # prints the response
print json.dumps(response.json(),indent=4),"\n" # Prints the response in JSON format


###Get a single task(GET METHOD)###

base_url="http://127.0.0.1:5000"
resp=requests.get(base_url+"/tasks/mKL3C5Kl")
print "###Getting a particular task result###"
print "response status code:",resp.status_code,"\n" # prints the response
print json.dumps(resp.json(),indent=4),"\n" # Prints the response in JSON format

###Create a task (POST METHOD)###

base_url="http://127.0.0.1:5000"
payload={"task": "add task","completed": False}
res=requests.post(base_url+"/tasks",json=payload)
print "###creating a new task result###"
print "response status code:",res.status_code,"\n" # prints the response
print json.dumps(res.json(),indent=4),"\n" # Prints the response in JSON format

###Modifies an existing task (PUT METHOD)###

base_url="http://127.0.0.1:5000"
payload={"task": "add task","completed": False}
re=requests.put(base_url+"/tasks/ZSjoZRQD",json=payload)
print "###Updating existing task result###"
print "response status code:",re.status_code,"\n"
print json.dumps(re.json(),indent=4),"\n"

### Mark an existing task as completed (POST METHOD)###

base_url="http://127.0.0.1:5000"
res1=requests.post(base_url+"/tasks/EOY6bdEi/completed")
print " ###Mark an existing task as completed result###"
print "response status code:",res1.status_code,"\n" # prints the response
print json.dumps(res1.json(),indent=4),"\n" # Prints the response in JSON format



### Mark an existing task as incomplete (POST METHOD)###

base_url="http://127.0.0.1:5000"
res2=requests.post(base_url+"/tasks/0AVAfIup/completed")
print " ###Mark an existing task as incomplete result###"
print "response status code:",res2.status_code,"\n" # prints the response
print json.dumps(res2.json(),indent=4),"\n" # Prints the response in JSON format


### Delete an existing task (DELETE METHOD)###

base_url="http://127.0.0.1:5000"

res3=requests.delete(base_url+"/tasks/pJk5qGZr")
print " ###Delete an existing task result###"
print "response status code:",res3.status_code,"\n" # prints the response
print json.dumps(res3.json(),indent=4),"\n" # Prints the response in JSON format





