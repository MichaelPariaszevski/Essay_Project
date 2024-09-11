import requests
import json

headers = {"X-ELS-APIKey": "d643c884a55db5728fc21a973b6c7746"}

params = {
        "query": "machine learning", 
        #   "view": "COMPLETE"
          }

response_2=requests.get(url = "https://api.elsevier.com/content/search/scopus", params = params, headers = headers) 

print(response_2.status_code)
print("-" * 50) 
print(response_2.content)
print(" # " * 100)

# json_output = json.dumps(response_2) 

print(response_2.json())

print(" # " * 50) 

# print()