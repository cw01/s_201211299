import os
import src.mylib
import requests
import re
import json
_url='http://openAPI.seoul.go.kr:8088'

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties2')
key=src.mylib.getKey(keyPath)

_key=str(key['dataseoul'])
_type='json'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
_api= _url+"/"+_key+"/"+_type+"/"+_service+"/"+str(_start_index)+"/"+str(_end_index)+"/"+_use_mon
data=requests.get(_api).text
jd = json.loads(data)
#print jd['STATION_NM']
#for key,value in jd.items():
#    print "---",key,value

print jd['CardSubwayStatisticsService']['row'][0]
#n=len(jd['SearchSTNBySubwayLineService']['row'])
#for i in range(0,n):
#    print jd['SearchSTNBySubwayLineService']['row'][i]
for item in jd['CardSubwayStatisticsService']['row']:
    print item.keys()
    for i in item.keys():
        if i=='STATION_NM':
            print ''.join(item.values())
            print item.values()[1]