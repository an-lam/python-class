# python3 version, derived from python2 version https://gist.github.com/dergachev/7028596
#
# taken from http://www.piware.de/2011/01/creating-an-https-server-in-python/
# generate server.xml with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
# run as follows:
#    python3 simple-https-server.py
# then in your browser, visit:
#    https://localhost:4443
"""
-bash-3.2$ openssl req -new -x509 -keyout server.pem -out server.pem -days 3650 -nodes
Generating a 1024 bit RSA private key
..++++++
.........................++++++
writing new private key to 'server.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [GB]:US
State or Province Name (full name) [Berkshire]:California
Locality Name (eg, city) [Newbury]:San Jose
Organization Name (eg, company) [My Company Ltd]:Lamsoftware LLC
Organizational Unit Name (eg, section) []:
Common Name (eg, your name or your server's hostname) []:AnLamServer
Email Address []:


-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCzjAu0gJwYDYJ3qOTdRQg7IOWInGvefymxmMc2QJ/dAfpJoYDe
kcpriHgfyi+cLmXRMQKPJ4YaZa5oR8lzPg/JYEtu+b9g3W8fGE0aQ9HpovZ7c7j8
E3n3lN0tzI8GWJqhSSIGaB5sQU6j7uxiC4jg+qWhvuiR0oqStUsnEVLo5QIDAQAB
AoGAKysXwV1OqmXNIZIE/MJVOUouhcr+EG/IiX+vHfcpuIx6LevbvSeWYIZeQ15s
VgO9zS8Ya2zYTE54QXBJGiEo0B3nRHFBrBkKZfpt77SGwrtkQJGQIpAKOPPsofNy
oh0JAQvXiI/Ms0d63mjEzrKAHHXJNdUA/A27Z6sdKJ2K010CQQDdHw4E3h92M3BR
2l0mG45Buo0wgmakOoIuwxgiHswQF6zYpGjvJt4CfOIinlTb6gx4RsNaq1n0d+5R
+KhaXTybAkEAz941w6JXoisUBxhrvq1zFNNuqeGYTrFhgqugAWn61C7T7qMjeGTl
HSMwAXHJanP4yjgT43yUYYzgTCxml9cIfwJAJ18BKwK1zWEJTbm4vjFH2hIyU4HU
bsdwKI1aPbEIGpFsmEJl4Lcl7oF37jwM1f9NaxkGbZ127d1w1K2WpEhXowJAV2hT
J06OlwySQWGNfQKmj61QrXLFfuGr5SyR/cY4yRxf1csX0Tpr9VKkjxbv4SmfBjmK
c3AhXNvGPYG2KkcrtQJBAKA/PUVpbSgwZ6i+Zfe3CONKOfEplVguMr9+u9R9catT
xOAVnw2GbEq/M5/RPy/Cuxa88eeD8kk1tXmbMvLldfg=
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIDEzCCAnygAwIBAgIJAP+qBfdY9YykMA0GCSqGSIb3DQEBBQUAMGUxCzAJBgNV
BAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMREwDwYDVQQHEwhTYW4gSm9zZTEY
MBYGA1UEChMPTGFtc29mdHdhcmUgTExDMRQwEgYDVQQDEwtBbkxhbVNlcnZlcjAe
Fw0xODA2MDYxNzAxMzNaFw0yODA2MDMxNzAxMzNaMGUxCzAJBgNVBAYTAlVTMRMw
EQYDVQQIEwpDYWxpZm9ybmlhMREwDwYDVQQHEwhTYW4gSm9zZTEYMBYGA1UEChMP
TGFtc29mdHdhcmUgTExDMRQwEgYDVQQDEwtBbkxhbVNlcnZlcjCBnzANBgkqhkiG
9w0BAQEFAAOBjQAwgYkCgYEAs4wLtICcGA2Cd6jk3UUIOyDliJxr3n8psZjHNkCf
3QH6SaGA3pHKa4h4H8ovnC5l0TECjyeGGmWuaEfJcz4PyWBLbvm/YN1vHxhNGkPR
6aL2e3O4/BN595TdLcyPBliaoUkiBmgebEFOo+7sYguI4Pqlob7okdKKkrVLJxFS
6OUCAwEAAaOByjCBxzAdBgNVHQ4EFgQUss6I1rt+6tkkP6PO6uXuuXw/w0kwgZcG
A1UdIwSBjzCBjIAUss6I1rt+6tkkP6PO6uXuuXw/w0mhaaRnMGUxCzAJBgNVBAYT
AlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMREwDwYDVQQHEwhTYW4gSm9zZTEYMBYG
A1UEChMPTGFtc29mdHdhcmUgTExDMRQwEgYDVQQDEwtBbkxhbVNlcnZlcoIJAP+q
BfdY9YykMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADgYEAIPfvzVsLD80f
V32+wMrqeygw1SDLNTX0G1132QjD2T4lJqdcTk7wBRfrasvP0SQhVXKXhe0rVrf3
hzj0fRtlETe5Eo9n5VDv8SrQh/Jn1zTq8EEVa86/JF8n049pkZ5E1+OeQnL96qxe
FBJVkCRuABu1gYD8P87S/rB0ioO40G8=
-----END CERTIFICATE-----


"""

import http.server
import ssl

httpd = http.server.HTTPServer(('127.0.0.1', 4443), http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='server.pem', server_side=True)
print("started https ...on port 4443")
httpd.serve_forever()