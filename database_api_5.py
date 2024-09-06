import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('Accept', 'application/vnd.crossref.unixsd+xml')]
r = opener.open('http://dx.doi.org/10.12968/hmed.2024.0244')
print (r.url)

