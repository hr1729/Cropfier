import urllib.request
import json
import time


READ_API_KEY='N5B0W4S1Z5CWEGAN'
CHANNEL_ID= '2055660'



TS = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                       % (CHANNEL_ID,READ_API_KEY))

response = TS.read()
data=json.loads(response)


    
b = data['field1']
    
print(b)
   
TS.close()
