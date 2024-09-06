import requests

def get_doi_bibtex(doi):
  base_url = f"https://doi.org/{doi}"
  headers = {
      "Accept": "text/bibliography; style=bibtex"
  }
  response = requests.get(base_url, headers=headers)

  if response.status_code == 200:
    return response.text.strip()
  else:
    print(response.status_code)
    print(response.text)
    return None

response = get_doi_bibtex("10.12968/hmed.2024.0244")

print(response)