import requests

def fetch_full_text_openalex(query):
    url = f"https://api.openalex.org/works?filter=title.search:{query}"
    response = requests.get(url)
    papers = response.json()['results']
    
    full_texts = []
    for paper in papers:
        # print(paper)
        if 'full_text' in paper:
            full_texts.append(paper['full_text'])
    
    return full_texts

query = "math"
full_texts = fetch_full_text_openalex(query)
for text in full_texts:
    print(text)