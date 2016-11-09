#!/usr/bin/python

#Robots.txt tool
import sys
import os

catalogs = ["admin",
            "log",
            "about",
            "manage",
            "manager",
            "panel"
            ]


def parse_robots(res):
    for line in res.readlines():
        for c in catalogs:
            if c in line:
                print "{} Found !".format(c)


def main():
    url = sys.argv[1]
    os.popen("rm -f robots.txt")
    os.popen("wget %s/robots.txt" % (url))

    res = file("robots.txt","r")
    if res:
        parse_robots(res)

    print "Analyze Completed!"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print "enter url:"



