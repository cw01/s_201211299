import os
import src.mylib
import requests
import re

_url='http://openAPI.seoul.go.kr:8088'

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties2')
key=src.mylib.getKey(keyPath)

_key=str(key['dataseoul'])
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
_api= _url+"/"+_key+"/"+_type+"/"+_service+"/"+str(_start_index)+"/"+str(_end_index)+"/"+_use_mon
p=re.compile('<RIDE_PASGR_NUM>(.*)</RIDE_PASGR_NUM>')
p1=re.compile('<ALIGHT_PASGR_NUM>(.*)</ALIGHT_PASGR_NUM>')
p2=re.compile('<LINE_NUM>(.*)</LINE_NUM>')
p3=re.compile('<SUB_STA_NM>(.*)</SUB_STA_NM>')

response = requests.get(_api).text

res=p.findall(response)
res1=p1.findall(response)
res2=p2.findall(response)
res3=p3.findall(response)

for i,node in enumerate(res):
    print '호선 이름 :',res2[i]
    print '역 이름 :',res3[i]
    print '승차 총 :',node
    print '하차 총 :',res1[i]
    print '----------------'