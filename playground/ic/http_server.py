#!/usr/bin/python3
import socketserver
from http.server import BaseHTTPRequestHandler
import json


class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):  # !important to use 'do_POST' with Capital POST
        request_headers = self.headers
        print(request_headers)

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        buildings = []
        for i in range(100):
            buildings.append({
                'building_id': f'b_{i}',
                'building_name': f'building_name_{i}',
                'latitude': i + 0.3,
                'longitude': i + 0.4})

        abc = {'type': 'buildings_by_user_id_request',
               'buildings': buildings}
        self.wfile.write(json.dumps(abc).encode('utf-8'))


try:
    print('lololo')
    httpd = socketserver.TCPServer(("localhost", 13337), MyHandler)
    httpd.serve_forever()
finally:
    print('lololo')
    httpd = socketserver.TCPServer(("localhost", 13337), MyHandler)
    httpd.server_close()
