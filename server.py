import SocketServer
import SimpleHTTPServer
import time
import urlparse

"""
run with: python server.py
"""

PORT = 8000
IP = ''

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/timestamp'):
            masterTime = time.time() * 1000

            parsed_path = urlparse.urlparse(self.path)
            clientTime = parsed_path.query.split('=')[1]

            diff = int(masterTime) - int(clientTime)

            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(diff)
        else:
            pass
        return

httpd = SocketServer.ThreadingTCPServer((IP, PORT),CustomHandler)

print 'Port =',PORT
httpd.serve_forever()
