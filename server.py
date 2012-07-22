import SocketServer
import SimpleHTTPServer
from datetime import datetime
import urlparse
import py.test

PORT = 8000
IP = ''

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/timestamp'):
            time = datetime.now()

            parsed_path = urlparse.urlparse(self.path)
            clientUnixTime = parsed_path.query.split('=')[1]
            clientTime = datetime.fromtimestamp(int(clientUnixTime)).strftime('%Y-%m-%d %H:%M:%S')

            print time
            print clientTime

            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(clientTime)
        else:
            pass
        return

httpd = SocketServer.ThreadingTCPServer((IP, PORT),CustomHandler)

print 'Port =',PORT
httpd.serve_forever()
