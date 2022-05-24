from http.server import HTTPServer, BaseHTTPRequestHandler
from bs4 import BeautifulSoup


with open('index.html', 'r') as file:
    soup = BeautifulSoup(file, "html.parser")
    # print(soup)


class WebPhoneBook(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        # html1 = html.replace('{}', """    <tr>
#     <td align="left">John</td>
#     <td align="left">112</td>
# </tr>""")
        self.wfile.write(soup.encode())
        # app1: add 3 users with phone number

    def do_POST(self):
        print(self.headers['name'])
        print(self.headers['number'])
        # print(self.rfile.read(100))

http_server = HTTPServer(('localhost', 8080), WebPhoneBook)
http_server.serve_forever()