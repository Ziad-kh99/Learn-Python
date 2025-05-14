# import BaseHTTPServer     # This is not available yet in Python-3
import http.server

class RequestHandler(http.server.BaseHTTPRequestHandler):
    '''
        Handle HTTP requests by returning a fixed page.
    '''

    # page is class-level variable containing the response body(text):
    page = b'''          
<html>
    <head>
        <title>Fixed Test Page</title>
    <head>
    <body>
        <h1>Hello, Web!</h1>
    </body>
</html>
    '''

    # Handle a GET request:
    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(self.page)))
        self.end_headers()
        self.wfile.write(self.page)


if __name__ == '__main__':
    serverAddress = ('', 8080)        # (IP-Address, Port-NO) 
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()