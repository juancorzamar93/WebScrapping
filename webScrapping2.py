#Segunda version
import urllib.request
import sys

if len(sys.argv) !=4:
    raise SystemExit('Usage: webScrapping2.py term page_number per_page')

term = sys.argv[1]   #"artificial intelligence"
page_number = sys.argv[2]   #1
per_page = sys.argv[3]  #20

u = urllib.request.urlopen('https://www.ted.com/search?page={}&per_page={}&q={}'.format(page_number, per_page, term.replace(" ", "+") ))
data = u.read()

from lxml import html
doc = html.document_formatstring(data)

for title in doc.cssselect("article.search_result h3 a"):
    print(title.text_content())
