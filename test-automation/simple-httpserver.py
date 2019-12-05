#!/usr/bin/env python
"""
HTTP Tutorial:
https://pymotw.com/3/http.server/
"""
import os

import yaml
from http.server import BaseHTTPRequestHandler, HTTPServer

from ssh_connection import SSHconnection

hostname = '172.16.0.21'
port = 22
username = 'pi'
password = 'anlam2018'


#Create custom HTTPRequestHandler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    #handle GET command
    def do_GET(self):
        # rootdir = "C:/Users/lama2/PycharmProjects/automation"
        rootdir = "C:/Users/lama2/PycharmProjects/test-automation"

        print("file name from client: {}".format(self.path))
        try:
            if self.path.endswith("/"):
                filename = "index.html"
            else:
                filename = rootdir + self.path

            f = open(filename)

            #send code 200 (OK) response
            self.send_response(200)

            #send header first
            self._set_headers()

            # Example: URL: localhost/config_file
            #send file content to client
            self.wfile.write(f.read().encode())
            f.close()
            return
            
        except IOError:
            self.send_error(404, 'file not found')

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()

        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length).decode() # <--- Gets the data itself
        print("data from client: {} ".format(post_data))

        # result = self.process(post_data)
        result = self.process_all(post_data)
        response = "<html><body><ol>"
        keylist = result.keys()
        for key in keylist:
            response += "<li>" + key + ": " + result[key] + "</li>"
        response += "</ol></body></html>"

        self.wfile.write(response.encode())
        print("incomming http: ", self.path)
        self.send_response(200)

    """ Process multiple test cases from client
    """

    def process_all(self, request):
        ssh_con = SSHconnection(hostname, username, password, port)
        print("request = " + request)

        test_names = request.split("&")

        result = {}
        print(test_names)
        for test in test_names:
            test = test.replace("testcase=", "")
            print(test)
            if test.find("test_ls") != -1:
                out, err = ssh_con.execute_command("ls /home/pi")
                print("output from 'ls /home/pi': " + out)
                result[test] = out
            elif test.find("test_cd") != -1:
                out = " "
                #out, err = ssh_con.execute_command("cd /home")
                out, err = ssh_con.execute_command("cat /home/pi/test.txt")
                print("output from 'cat /home/pi/test.txt': " + out)
                if err != "":
                    result[test] = err
                else:
                    result[test] = out
            else:
                result["result"] = "Unknown test case"

        print(result)

        ssh_con.close()
        return result

    """ Process request from client
    """
    def process(self, request):
        ssh_con = SSHconnection(hostname, username, password, port)
        print("request = " + request)

        # Execute test based on test case name
        if request.find("test_ls") != -1:
            result, err = ssh_con.execute_command("ls /home/pi")
            print("output from RP: " + result)
        else:
            result = "Unknown test case"

        ssh_con.close()
        return result


def run():
    print('http server is starting on port 80...')
    try:
        #by default http server port is 80
        server_address = ('127.0.0.1', 80)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        print('http server is running...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        httpd.socket.close()

if __name__ == '__main__':
    # Load config file
    with open("raspberry_config", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    device = cfg['mydevice']
    print(device)
    hostname = cfg['mydevice']['ip']
    port = cfg['mydevice']['port']
    username = cfg['mydevice']['username']
    password = cfg['mydevice']['password']
    print("mydevice: {}".format(cfg['mydevice']))

    run()
