import urllib.request, urllib.parse, urllib.error

print("Get the image from: http://data.pr4e.org/cover3.jpg ")
print("Write to local file: 'cover3.jpg'")
img = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg").read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()
print("Check your file: 'cover3.jpg'")
