# coding: utf-8
import re
import requests
rResponse = requests.get('http://python.org/')
_html = rResponse.text

#p=re.compile('http://.+"')
p=re.compile('href="(http://.*?)"')
nodes=p.findall(_html)
print "http url은 몇 개?",len(nodes)
for i, node in enumerate(nodes):
    print i, node