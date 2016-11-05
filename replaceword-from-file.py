#!/usr/bin/python

# Word Replacer from File ;) Usefull while Brute

a = raw_input("Enter the Word to Replace with Item name in list : \n")
b = raw_input("Enter New Word After Replace\n")

inputfile = raw_input("Enter Input File : ")
outputfile = raw_input("Enter the OutputFile Name: ")

with open(inputfile) as input, open(outputfile,"w") as output:
		for line in input:
			output.write(line.replace(a,b))
