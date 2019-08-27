import requests
import datetime
from bs4 import BeautifulSoup
import pprint

URL = 'link' #ex:)http://search.sinmun.com/search/total.search?query=
HEADERS = {
    'User-Agent' : 'Mozixxx/5.0 (Windowx xx 10.0; xin64; x64) ApxxxWebKit/5xx.36 (xHTML, like Geckx) Chrxxe/7x.0.38x9.100 Saxxxx/53x.36'
}

query = "Your Keyword"
sdate = datetime.date.today() - datetime.timedelta(days = 7)
edate = datetime.date.today()

PARAMS = {
    'query':query,
    'pageno' : 0,
    'orderby' : 'docdatetime',
    'sdate' : sdate.strftime('%Y.%M.%D'),
    'edate' : edate.strftime('%Y.%M.%D')
}

req = requests.get(URL, PARAMS, headers=HEADERS)
print(req)
soup = BeautifulSoup(req.content, 'lxml')
req.close()
print(soup)
search_news = soup.find('div', attrs = {'class':'search_news_box'})

for article in search_news.findAll('dl'):
    head = article.dt.a
    print(head)
    desc = article.find('dd', attrs={'class':'desc'})  
    print(desc)
    print(" ")
    print(" ")