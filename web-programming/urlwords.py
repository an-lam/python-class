import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        # get() returns default value 0 if word is not found
        counts[word] = counts.get(word, 0) + 1
print(counts)