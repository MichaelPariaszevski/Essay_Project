# import urllib, urllib.request

# url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
# data = urllib.request.urlopen(url)
# print(data.read().decode('utf-8'))

from paperscraper.pubmed import get_and_dump_pubmed_papers
covid19 = ['COVID-19', 'SARS-CoV-2']
ai = ['Artificial intelligence', 'Deep learning', 'Machine learning']
mi = ['Medical imaging']
query = [covid19, ai, mi]

response = get_and_dump_pubmed_papers(query, output_filepath='covid19_ai_imaging_2.jsonl', start_date = '2022/07/20')

print(type(response))

