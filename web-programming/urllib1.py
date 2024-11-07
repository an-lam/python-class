import urllib.request

# Similar to open a file on your hard drive
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    #print(line)
    print(line.decode().strip())