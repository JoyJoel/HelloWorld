from http.server import HTTPServer, CGIHTTPRequestHandler

server_addr = ('', 80)
server_obj = HTTPServer(server_addr, CGIHTTPRequestHandler)
server_obj.serve_forever()
