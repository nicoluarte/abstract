import urllib.request
import sys
from xml.dom import minidom
import os

# arglist to actual list
argList = list(sys.argv)
# calling the search query
p1 = "http://export.arxiv.org/api/query?search_query="
# actual phrase to search
p2 = argList[1]
# bananas
p3 = "&start=0&max_results="
# max_results
p4 = argList[2]
url = p1 + p2 + p3 + p4
data = urllib.request.urlopen(url).read()
document = minidom.parseString(str(data, encoding='utf-8'))
title = document.getElementsByTagName('title')
summary = document.getElementsByTagName('summary')
link = document.getElementsByTagName('id')
file = open(str(argList[1])+".txt", "w")
filename = str(argList[1]+".txt")
for s in range(0, len(summary)):
    file.write(title[s].firstChild.nodeValue + "\n\n" +
               link[s].firstChild.nodeValue + "\n\n" +
               summary[s].firstChild.nodeValue + "\n\n")

cmd = "pandoc -s " + filename + " -o " + str(argList[1]+".tex")
cmd2 = "pdflatex " + str(argList[1]+".tex")
os.system(cmd)
os.system(cmd2)
