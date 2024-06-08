#!/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPServerRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='text/plain'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
        elif self.path == '/data':
            self._set_headers(content_type='application/json')
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self._set_headers()
            self.wfile.write("OK".encode('utf-8'))
        elif self.path == '/info':
            self._set_headers(content_type='application/json')
            info = {"version": "1.0", "description": "A simple API"
                    "built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPServerRequestHandler)
    print('Starting server on port 8000...')
    httpd.serve_forever()

    if __name__ == '__main__':
        run()