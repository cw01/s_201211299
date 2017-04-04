import urllib2
from bs4 import BeautifulSoup
url = 'http://www.google.com/search?q=python'
headers = {'User-Agent':'Mozilla 5.0'}
request = urllib2.Request(url,None,headers)
response = urllib2.urlopen(request)
html = response.read()
bs = BeautifulSoup(html,'lxml')
bsSelect = bs.select('#ires > ol > div > h3 > a')
i = 0
print len(bsSelect)
for i,node in enumerate(bsSelect):
    print i,node.get('href').split('=')[1]