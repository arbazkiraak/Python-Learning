#!/usr/bin/python

import sys,time

if len(sys.argv) <  3:
	print """ Usage : list-generate.py name wordlist"""
  print """ For Save : list-generate.py name wordlist > output.txt"""
	sys.exit(0)


name = sys.argv[1]

word = sys.argv[2]

time.sleep(2)

take = open(word,"r").readlines()
for i in take:
	i= i.rstrip('\n')
	i= i.rstrip('\r')
	print str(i)+"."+str(name)
