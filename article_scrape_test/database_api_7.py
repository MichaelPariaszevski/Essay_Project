import requests 

def search(query, url): 
    params = {"query": query} 
    headers = {"X-ELS-APIKey": "d643c884a55db5728fc21a973b6c7746"}
    response = requests.get(url = url, params = params, headers = headers)
    return response.status_code, response.content 

url = "https://api.elsevier.com/content/search/scidir"

print(search(query = "machine learning", url = url))
