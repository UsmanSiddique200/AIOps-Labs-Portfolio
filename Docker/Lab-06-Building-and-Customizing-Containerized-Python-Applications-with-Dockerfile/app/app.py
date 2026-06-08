#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
from datetime import datetime


class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Get environment variables with defaults
        app_name = os.environ.get('APP_NAME', 'Docker Python App')
        app_version = os.environ.get('APP_VERSION', '1.0.0')
        environment = os.environ.get('ENVIRONMENT', 'development')
        debug_mode = os.environ.get('DEBUG', 'false').lower() == 'true'

        response_data = {
            "application": {
                "name": app_name,
                "version": app_version,
                "environment": environment,
                "debug_mode": debug_mode
            },
            "message": f"Hello from {app_name}!",
            "timestamp": datetime.now().isoformat(),
            "status": "success",
            "container_info": {
                "hostname": os.environ.get('HOSTNAME', 'unknown'),
                "python_version": "3.11",
                "port": os.environ.get('PORT', '8080')
            }
        }

        self.wfile.write(json.dumps(response_data, indent=2).encode())


def run_server():
    port = int(os.environ.get('PORT', 8080))
    app_name = os.environ.get('APP_NAME', 'Docker Python App')

    server = HTTPServer(('0.0.0.0', port), SimpleHandler)

    print(f"Starting {app_name} on port {port}...")
    print(f"Environment: {os.environ.get('ENVIRONMENT', 'development')}")
    print(f"Debug mode: {os.environ.get('DEBUG', 'false')}")
    print(f"Access the application at http://localhost:{port}")

    server.serve_forever()


if __name__ == '__main__':
    run_server()
