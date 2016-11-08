#!/usr/bin/python

import requests,sys

a = raw_input("Please  Enter Text File of subdomains : ")

for url in open(a):
    try:
        r = requests.head(url.rstrip())
	print "------------------------------------------"
	print "Site Headers Being Checked:", url
        if 'Strict-Transport-Security' in r.headers:
                print "Strict-Transport-Security:", r.headers['Strict-Transport-Security']
        else:
                print "Strict-Transport-Security Not Present"
	if 'X-Xss-Protection' in r.headers:
		print "X-Xss-Protection:", r.headers['X-Xss-Protection']
	else: 
		print "X-Xss-Protection Not Present"
        if 'X-Content-Type-Options' in r.headers:
                print "X-Content-Type-Options:", r.headers['X-Content-Type-Options']
        else: 
                print "X-Content-Type-Options Not Present"
	if 'X-Frame-Options' in r.headers:
		print "X-Frame-Options:", r.headers['X-Frame-Options']
	else:
		print "X-Frame-Options Not Present"
        if 'Content-Security-Policy' in r.headers:
                print "Content-Security-Policy:", r.headers['Content-Security-Policy']
        else: 
                print "Content-Security-Policy Not Present"
	if 'Public-Key-Pins' in r.headers:
		print "Public-Key-Pins:", r.headers['Public-Key-Pins']
	else:
		print "Public-Key-Pins Not Present"
	print "------------------------------------------","\n"
  
    except:
        print "Unknown Exception:",sys.exc_info()[0]
	raise
