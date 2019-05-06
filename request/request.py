# importing the requests library 
import requests 
import sys

# api-endpoint 
url = "http://demo7862839.mockable.io/contacts"
gid = input('Ingrese el gid')
  
# defining a params dict for the parameters to be sent to the API 
params = {'gid':gid}
  
# data to be sent to api as data or boddy 
contact_list = [{'FirstName': 'Michael', 'LastName': 'Kirk', 'phone': '810-292-9388'}]


# sending post request and saving the response as response object 
post_response = requests.post(url = url, params = params, data = contact_list) 

# extracting data in json format 
data_post = post_response.json()

# Print data
print(data_post)  


# # sending get request and saving the response as response object 
# get_response = requests.get(url = url, params = params) 
  
# # extracting data in json format 
# data_get = get_response.json()  

# print(data_get) 