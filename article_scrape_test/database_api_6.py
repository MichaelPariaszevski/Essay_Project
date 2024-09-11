import requests 

doi = "10.1016/j.ibusrev.2010.09.002"

params = {"view": "FULL"}

headers = {"X-ELS-APIKEY": "d643c884a55db5728fc21a973b6c7746"}

response = requests.get(url = f"https://api.elsevier.com/content/article/doi/{doi}?httpAccept=text/xml", headers = headers)

print(type(response))
print(response.status_code)
print(response)
print(response.content)