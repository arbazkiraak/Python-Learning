#!/usr/bin/python

import requests
from optparse import OptionParser
import sys

print "Crossdomain Checker\n"
print "[x]" * 10

def CrossDomain(host):
      if "http" in host or "https" in host:
        url = host
      else:
        url = "http://"+url
      try:
         req = requests.get(url+"/crossdomain.xml",timeout=3)
         print "Testing : "+url
         if "cross-domain-policy" in req.text:
          print "Cross domain Found for : "+url
         cross = open("output.txt","a")
         cross.write("[+] Cross Domain url [+]\n\n\n")
         for text in url.text:
         cross.write(text)
         cross.write("\n\n\n\n")
         cross.close()
          
         
