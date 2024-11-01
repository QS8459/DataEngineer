from http.server import HTTPServer, BaseHTTPRequestHandler;

class SimpleHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200);

        self.send_header("Content-type", 'text/html');
        self.end_headers();

        self.wfile.write(b'Custom Text');


def run(server_class = HTTPServer, handler_class = SimpleHttpRequestHandler, port = 8000):
    server_address = ('127.0.0.1', port);

    httpd = server_class(server_address, handler_class);
    print(f"Staring httpd server on port {port}")
    httpd.serve_forever();

if __name__ == "__main__":
    run()
