import requests

def fetch_full_text_core(query):
    url = f"https://api.core.ac.uk/v3/discover"
    params = {
              "title": "diabetes"
              }
    headers = {"Authorization": "Bearer [BWQPj814VdEeOH2KiXS3wm50fLlCUYbz]"}
    response = requests.post(url, params = params)
    print(response.status_code)
    papers = response.json()
    
    full_texts = []
    for paper in papers['data']:
        if 'fullTextUrl' in paper and paper['fullTextUrl']:
            full_texts.append(paper['fullTextUrl'])
    
    return full_texts

query = "diabetes"
full_texts = fetch_full_text_core(query)
for text in full_texts:
    print(text)