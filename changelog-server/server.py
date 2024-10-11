import os, re
import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs


class CLHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        DEMARCATION = "******************************************************"
        # Sending an '200 OK' response
        self.send_response(200)

        # Setting the header
        self.send_header("Content-type", "text/html")

        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()

        # List all files in the directory
        path = "./logs/"
        files = os.listdir(path)

        # Initial html tag
        html = "<html><head></head><body>"

        # Print the files
        content = ""
        for file in files:
            if re.match(r'change_log_\d{14}', file):
                content = content + f"<br>{DEMARCATION}<br>{file}<br><br>{DEMARCATION}<br>"
                with open( path+ file, "r") as fp:
                    for line in fp:
                        content = content + "<p>" + line + "</p>"
                # print(file)

        # Conclusive tags
        html = html + content + "</body></html>"

        # Writing the HTML contents with UTF-8
        self.wfile.write(bytes(html, "utf8"))

        return

# Create an object of the above class
handler_object = CLHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
