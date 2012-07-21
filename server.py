import SocketServer
import SimpleHTTPServer
import time
PORT = 8000
IP = ''
def sayHello():
    return 'Hello'

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
    	print 'path is ', self.path
        if self.path=='/hello':
            time = time.time()
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(sayHello())
            return
        else:
            self.wfile.write("Error")

httpd = SocketServer.ThreadingTCPServer((IP, PORT),CustomHandler)

print 'Port =',PORT
httpd.serve_forever()
