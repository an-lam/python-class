from http.server import BaseHTTPRequestHandler, HTTPServer
import base64

auth_key = ""
retry_count = 0

class CustomHandler(BaseHTTPRequestHandler):
    ''' Main class to present webpages and authentication. '''
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        #global auth_key
        auth_key = "YXVsYWM6YWJj"
        print(self.headers['Authorization'])
        #id_password = "aulac:abc".encode()
        #auth_key = base64.b64encode(id_password)
        #print("auth_key: " + str(auth_key))
        # Present frontpage with user authentication.
        if self.headers['Authorization'] == None:
            self.do_AUTHHEAD()
            self.wfile.write(bytes('no auth header received', 'UTF-8'))
        elif self.headers['Authorization'] == 'Basic ' + auth_key:
            print("file name from client: {}".format(self.path))
            self.process(self.path)
        else:
            print("Incorrect user/password: {}".format(self.headers['Authorization']))
            retry_count += 1
            if retry_count >= 3:
                self.do_AUTHHEAD()
                self.wfile.write(bytes(self.headers['Authorization'], 'UTF-8'))
                self.wfile.write(bytes(' You typed incorrect password > 3 times', 'UTF-8'))
            else:
                self.do_AUTHHEAD()
                self.wfile.write(bytes(self.headers['Authorization'], 'UTF-8'))
                self.wfile.write(bytes(' Incorrect user/password!', 'UTF-8'))


    def process(self, path):
        #rootdir = "C:/Users/lama2/PycharmProjects/automation"
        rootdir = "C:/Users/lama2/PycharmProjects/test-automation"
        print("file name from client: {}".format(path))
        try:
            if path.endswith("/"):
                filename = "index.html"
            else:
                filename = rootdir + self.path

            f = open(filename)

            # send code 200 (OK) response
            self.send_response(200)

            # send header first
            self.do_HEAD()

            # send file content to client
            self.wfile.write(f.read().encode())
            f.close()
            return

        except IOError:
            self.send_error(404, 'file not found')


def main():
   try:
      # Create a HTTP server and specify our CustomHanler to handle requests
      # Point browser to: http://localhost:8888
      #  Specify user: aulac, password: abc
      port = 8888
      server_address = ('127.0.0.1', port)
      httpd = HTTPServer(server_address, CustomHandler)
      print ("started httpd...on port {}, user: 'aulac', password: 'abc' \n".format(port))
      httpd.serve_forever()
   except KeyboardInterrupt:
      print ("^C received, shutting down server")
      httpd.socket.close()

if __name__ == '__main__':
    main()