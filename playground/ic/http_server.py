#!/usr/bin/python3
import datetime
import random
import socketserver
from http.server import BaseHTTPRequestHandler
import json


class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):  # !important to use 'do_POST' with Capital POST
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        if post_body['type'] == 'buildings_by_user_id_request':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            buildings = []
            for i in range(10):
                buildings.append({
                    'building_id': f'b_{i}',
                    'building_name': f'building_name_{i}',
                    'latitude': (45.815399
                                 + random.uniform(0.000_001, 0.000_009)),
                    'longitude': (15.966568
                                  + random.uniform(0.000_001, 0.000_009))})
            body = {'type': 'buildings_by_user_id_request',
                    'buildings': buildings}
            self.wfile.write(json.dumps(body).encode('utf-8'))

        elif post_body['type'] == 'building_info_request':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            buildings_info = []
            times = [datetime.datetime.now(datetime.timezone.utc)
                     - datetime.timedelta(minutes=15 * i)
                     for i in range(100)]
            times = sorted(times)
            for building_id in post_body['building_ids']:
                building_info = {'building_id': building_id,
                                 'info': []}
                for t in times:
                    building_info['info'].append({
                        'value': 100 + random.uniform(100, 300),
                        'timestamp': t.isoformat()})
                buildings_info.append(building_info)

            body = {'type': 'building_info_response',
                    'buildings_info': buildings_info}
            self.wfile.write(json.dumps(body).encode('utf-8'))
        else:
            self.send_response(404)


try:
    print('starting')
    httpd = socketserver.TCPServer(("localhost", 13337), MyHandler)
    httpd.serve_forever()
finally:
    print('closing')
    httpd = socketserver.TCPServer(("localhost", 13337), MyHandler)
    httpd.server_close()
