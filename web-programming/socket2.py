import socket

# This is using HTTP 1.0 - not all servers support the oldest protocol
# Try http://data.pr4e.org/romeo.txt if your server fails.
#       nblox.txt
# url = input('Enter (example: http://westvalley.edu): ')
url = "http://data.pr4e.org/mbox.txt"
#url = "https://deanza.edu"
words = url.split('/')
print("words: ", words)
host = words[2]
print("host = ", host)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
#mysock.connect((host, 443))
mysock.send(("GET " + url + " HTTP/1.0\r\n\r\n").encode())

i = 1
while True:
    data = mysock.recv(4512)
    print(" i: ", i)
    i += 1
    if (len(data) < 1):
        break
    print(data.decode(), end='')

mysock.close()
