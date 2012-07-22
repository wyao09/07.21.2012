import SocketServer
import SimpleHTTPServer
from datetime import datetime
PORT = 8000
IP = ''
def sayHello():
    return 'Hello'

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/timestamp':
            time = datetime.now()
            clientTime = self
            #diff = time - clientTime

            print dir(self.request)

            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(sayHello())
        return

httpd = SocketServer.ThreadingTCPServer((IP, PORT),CustomHandler)

print 'Port =',PORT
httpd.serve_forever()
