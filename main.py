import http.server
import socketserver
import json


class Handler (http.server.SimpleHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        self.wfile.write(json.dumps({'message': 'Hello World'}).encode('utf-8'))
        # return http.server.SimpleHTTPRequestHandler.do_GET(self)


def run(server_class=socketserver.TCPServer, handler_class=Handler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
