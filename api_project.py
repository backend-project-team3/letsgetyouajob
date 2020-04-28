#Hey team! This is my practice API requests. I have placed them by URL/ Location and roles.


#This request is for the url we spole about earlier today
import requests
response = requests.get('https://jobs.github.com/positions.json?location=bay+area')
data = response.json()
print(data)


#This is to get the roles that users can apply for.
for item in data:
   print(item['title'])
   


#This path shows the locations around the bay area that are hiring.
#(I'm still working on getting "tokyo" out the data)
for item in data:
   print(item['location'])


# import requests
# response = requests.get('https://jobs.github.com/positions.json?description=python&full_time=true&location=sf')
# data = response.json()
# print(data)

# rates = data['full_time']
# for code, rate in rates.items():
#     print(code, rate)

import requests

response = requests.get('https://jobs.github.com/positions.json?title=javascript&full_time=false&page=1/')
data = response.json()

print(data)
for item in data:
    print(item['title']+'-'+ item['type'])
print(len(data))


