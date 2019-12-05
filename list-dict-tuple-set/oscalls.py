import os

ip = "www.google.com"
response = os.system("ping {}".format(ip))
if response == 0:
    print("www.google.com is up")
else:
    print("www.google.com is down")
