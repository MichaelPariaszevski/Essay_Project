import requests 

def get_dois(query): 
    url = "https://api.crossref.org/works" 
    params = { 
              "query": query, 
              "rows": 10
              }
    response = requests.get(url, params=params) 
    data = response.json() 
    for i in data["message"]["items"]: 
        print("-" * 50) 
        print(i["URL"])
        print("-" * 50)

print(get_dois(query="machine learning"))