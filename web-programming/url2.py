import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        # if key not found get return default value: 0
        counts[word] = counts.get(word, 0) + 1
print(counts)
