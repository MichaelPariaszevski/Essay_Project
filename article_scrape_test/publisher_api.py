import requests

def fetch_full_text_elsevier(query, api_key):
    # headers = {"X-ELS-APIKey": api_key}
    url = f"https://api.elsevier.com/content/search/sciencedirect"
    params = {"query": query}
    headers = {"X-ELS-APIKey": "d643c884a55db5728fc21a973b6c7746"}
    response = requests.get(url, headers = headers, params = params)
    print(response.status_code)
    papers = response.json()
    
    full_texts = []
    for paper in papers['search-results']['entry']:
        if 'link' in paper:
            for link in paper['link']:
                if link['type'] == 'text/html':
                    full_texts.append(link['href'])
    
    return full_texts

query = "machine learning"
api_key = "d643c884a55db5728fc21a973b6c7746"
full_texts = fetch_full_text_elsevier(query, api_key)
for text in full_texts:
    print(text)