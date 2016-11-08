# -*- coding: utf-8 -*-
import requests
import string
import optparse
import sys

def grabheaders(url):
    print "[+]Checking " +str(url)
    try:
        r = requests.get(url) #request user provided url
    except Exception, e:
        print e  #error handling
    if 'X-Xss-Protection' not in r.headers: #if there is no X-Xss-Protection key
        print "[-]Site " +str(url)+ " may be vulnerable to XSS"
    elif "1" in (r.headers['X-Xss-Protection']): #if the X-Xss-Protection key is =1 
        print "[+]Site " +str(url)+ " has XSS Protection"
    else:                                        #all other circumstances other than 1 (ie 0)
        print "[-]Site " +str(url)+ " may be vulnerable to XSS"

def main():

    print ' by threebones \n https://github.com/threebarber\n'

    parser = optparse.OptionParser() #create parser object called "parser"

    parser.usage = "[+] Usage:      xsscheck.py -u <url> " \
                   "\n[+] Example:    xsscheck.py -u http://google.com " #add usage for "parser" object as well as example

    parser.add_option(
            '-u','--url',dest='url',type='string',help='see usage') #add url options as -u or --url

    (options, args) = parser.parse_args(sys.argv) #finalize parsing portion
 
    url = options.url #set var url to value of url option in parser

    if (url) == None: #require a url or target 
        print parser.usage
        exit(0) #check to make sure required params were assigned a value - if not, exit
    
    grabheaders(url) #run grabheader function to check for possibility of xss

if __name__ == '__main__':
    main()
