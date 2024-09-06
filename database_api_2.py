import requests

def get_full_text(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'message' in data:
            print(data["message"])
            return data['message']
    return None

doi = "10.12968/hmed.2024.0244"  # Replace with your DOI
metadata = get_full_text(doi)
if metadata:
    print("Title:", metadata.get('title'))
    print("URL:", metadata.get('URL'))
    print("-"*50) 
    print(metadata.keys())
    print(metadata["URL"])
else:
    print("DOI not found or access restricted.")
