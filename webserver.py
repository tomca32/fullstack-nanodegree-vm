from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class WebServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				seld.send_header('Content-type', 'text/html')
		except:

def main():
	try:
		port = 8080
		server = HTTPServer(('', port), WebServerHandler)
		print "Web server is running on port %s" % port
		server.serve_forever()
	except KeyboardInterrupt:
		print "^C entered, stopping web server..."
		server.socket.close()

if __name__ =='__main__':
	main()