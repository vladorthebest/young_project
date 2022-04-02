from http.server import HTTPServer, BaseHTTPRequestHandler

APP_HOST = 'localhost'
APP_PORT = 8080

class SimpleGetHandler(BaseHTTPRequestHandler):
    def _set_hendler(self):
        self.send_response(200)
        self.send_header("content-text", "text/html; charset = utf-8")
        self.end_headers()

    def _html(self, message):
        content = (
            f"<html>"
            f"<body>"
            f"<h1>{message}</h1>"
            f"</body>"
            f"</html>"
        )

        return content.encode("utf-8")
    
    def do_GET(self):
        self._set_hendler()
        message = "Hello World!"
        self.wfile.write(self._html(message))

def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (APP_HOST, APP_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run_server(handler_class=SimpleGetHandler)