import requests
from bs4 import BeautifulSoup as bs
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

res = requests.get('https://search.naver.com/search.naver?query=deepmind+pdf', headers=headers)
soup = bs(res.text, 'lxml')
pdfs = soup.select('a[href$=".pdf"]')

urls = []
for p in pdfs:
    urls.append(p['href'])

urls = set(urls)

for url in urls:
    response = requests.get(url, stream=True)
    filename = re.findall("[^/]*$", url)[0]
    print(url)

    f = open(filename, "wb")
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)