import requests 

def get_full_text(query): 
    query = query.replace("", "+") 
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5" 
    response = requests.get(url) 
    papers = response.text 
    return papers

print(get_full_text("machine learning"))