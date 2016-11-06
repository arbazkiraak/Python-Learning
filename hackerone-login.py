#!/usr/bin/python

import cookielib
import urllib
import urllib2

a = raw_input("Enter your Hackerone Email: ")

b = raw_input("Enter your Hackerone Password: ")

c = raw_input("Enter Auth_token From Login Page: ")

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
resp = opener.open("https://hackerone.com")

theurl = "https://hackerone.com/users/sign_in"
body = {
  'authenticity_token': c,
  'user[email]': a,
  'user[password]': b
}

txdata = urllib.urlencode(body)
txheaders = headers = {
    'Host': 'hackerone.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://hackerone.com/users/sign_in',
    'Connection': 'keep-alive',
}

try:
	req = urllib2.Request(theurl,txdata,txheaders)
	handle = opener.open(req)
	HTMLSource = handle.read()
	f = file("test.html","w")
	f.write(HTMLSource)
	f.close()

except IOError, e:
	print 'We failed to open "%s".' % theurl
	print "\n"
if hasattr(e, 'code'):
        print 'We failed with error code - %s.' % e.code
elif hasattr(e, 'reason'):
        print "The error object has the following 'reason' attribute :", e.reason
        print "This usually means the server doesn't exist, is down, or we don't have an internet connection."
        sys.exit()

else:
    print 'Here are the headers of the page :'
    print handle.info() 
