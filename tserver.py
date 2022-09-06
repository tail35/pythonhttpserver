from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import time

data = {'result': 'this is a test'}
host = ('10.0.16.185', 8888)

num = 0
class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        print("path:"+self.path)
        global  num
        if -1!=self.path.find("x20.ts"):
            #if 0==num:
            time.sleep(20.0)
            num+=1


        self.send_header('Access-Control-Allow-Origin', '*')#cross domain.
        if -1==self.path.find("m3u8"):
            print('ts')
            self.send_header('Content-type', 'video/mp2t')
        else:
            print('m3u8')
            self.send_header('Content-type', 'text/plain')
        
        filename = os.path.basename( self.path )
        print(filename)
        filename='D:\\tudycode\\pythoncode\\httpserver\\hls'+filename
        self.end_headers()

        with open(filename, "rb") as f:
            f_content = f.read()
            self.wfile.write(f_content)
        #video/mp2t text/plain application/json
    def do_POST(self):
        datas = self.rfile.read(int(self.headers['content-length']))

        print('headers', self.headers)
        print("do post:", self.path, self.client_address, datas)

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
