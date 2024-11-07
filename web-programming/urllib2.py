import urllib.request, urllib.parse, urllib.error

#url1 = "http://www.westvalley.edu"
url2 = "http://www.dr-chuck.com/page2.htm"
fhand = urllib.request.urlopen(url2)
for line in fhand:
    print(line.decode().strip())