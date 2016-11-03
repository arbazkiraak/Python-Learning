#!/usr/bin/python

#  usage python dir-arrange.py > outdir.txt
line = []
filtered = []

line = open("words.txt","r").readlines()

for l in line:
	if l.startswith("blog") is False:
		l = l.rstrip("\n")
		l = l.rstrip("\r")
		filtered.append(l)

for i in filtered:
	print i
