import http.server
import socketserver

port = 9000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print("Server at port", port)
    httpd.serve_forever()
