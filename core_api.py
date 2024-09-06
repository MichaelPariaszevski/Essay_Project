import requests

def fetch_full_text_core(query):
    url = f"https://core.ac.uk/api-v2/articles/search/{query}?page=1&pageSize=5&apiKey=BWQPj814VdEeOH2KiXS3wm50fLlCUYbz"
    response = requests.get(url)
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