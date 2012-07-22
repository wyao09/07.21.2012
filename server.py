import SocketServer
import SimpleHTTPServer
import time
import urlparse
import sys
from os import curdir, sep

"""
server.py [port (defaults to 8000)]
"""

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
IP = ''

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/timestamp'):
            masterTime = 1000 * time.time()

            parsed_path = urlparse.urlparse(self.path)
            pieces = parsed_path.query.split('=')
            clientTime = pieces[1] if len(pieces) >= 2 else 0

            diff = int(masterTime) - int(clientTime)

            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write('"%s|%lf"' % (diff,masterTime))
        elif self.path.startswith('/index.html'):
            f = open(curdir + sep + 'index.html')
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        else:
            f = open(curdir + self.path)
            self.send_response(200)
            self.send_header('Content-type','audio/mpeg')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        return

httpd = SocketServer.ThreadingTCPServer((IP, PORT),CustomHandler)

print 'Port =',PORT
httpd.serve_forever()
