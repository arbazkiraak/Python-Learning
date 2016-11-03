#!/usr/bin/python

#http://xxx-profile-images.s3.amazonaws.com/
#Amazon aws bucket list generator
#make sure to use good wordlist (common for dir)
import sys,time

if len(sys.argv) < 3:
	#""" Usage : list-generate1.py name wordlist"""
	sys.exit(0)

name = sys.argv[1]
word = sys.argv[2]
time.sleep(2)

take = open(word,"r").readlines()
for i in take:
	i = i.rstrip('\n')
	i = i.rstrip('\r')
	print "http://"+str(name)+"-"+str(i)+"."+"s3"+"."+"amazonaws.com"
