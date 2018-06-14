# -*- coding:utf-8 -*-

import time
import BaseHTTPServer

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header('Content-type', 'text/html')
		s.end_headers()

	def do_GET(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		s.wfile.write("<html><head><title>gaia python demoe</title></head>")
		s.wfile.write("<body><p>this is a demo.</p>")
		s.wfile.write("<p>You accessed path: %s</p>" % s.path)
		s.wfile.write("</body></html>")


def main():
	httpd = BaseHTTPServer.HTTPServer(('', 8001), MyHandler)
	print time.asctime(), "Server Starts - %s:%s" % ('', 8001)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	
	httpd.server_close()
	print time.asctime(), "Server Stops - %s:%s" % ('', 8001)

if __name__ == '__main__':
	main()