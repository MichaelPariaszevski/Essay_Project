import requests 

def get_full_text(dois): 
    full_texts = [] 
    for doi in dois: 
        response = requests.get(f'https://api.unpaywall.org/v2/{doi}?email=mpariaszevski@gmail.com')
        data = response.json() 
        if "full_text_url" in data and data["full_text_url"]: 
            full_texts.append(data["full_text_url"]) 
        else: 
            full_texts.append("Not available")
    return full_texts

dois = ["10.12968/hmed.2024.0244"]
full_texts = get_full_text(dois)
for text in full_texts:
    print(text)