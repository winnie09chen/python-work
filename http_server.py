import socket
import os.path


STATUS_MAP = {
    200: 'OK',
    404: 'NOT FOUND',
    502: 'SERVER '
}

MIME_MAP = {
    '.html': 'text/html; charset=utf-8',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.js': 'application/javascript',
}

class Handler:
    def __init__(self, root_dir):
        self.root = root_dir
    
    def handle(self, method, path, headers):
        status = 200
        headers = {}
        body = b''

        if method == 'GET':
            p = os.path.join(self.root, path[1:])
            print(p)
            if not os.path.exists(p):
                return 404, headers, body
            with open(p, 'rb') as fo:
                body = fo.read()
            _, ext = os.path.splitext(p)
            mime = MIME_MAP.get(ext, 'application/object')
            headers['Content-Type'] = mime
        return status, headers, body


def server(c, addr, handler):
    print(addr, 'connected')

    total = b''
    request = {}
    while True:
        data = c.recv(1024)
        if data.endswith(b'\r\n\r\n'):
            total += data
            break
        total += data

    req_lines = total.split(b'\r\n')
    method_line = req_lines[0].decode()
    method_parts = method_line.split()
    method = method_parts[0]
    path = method_parts[1]
    protocol = method_parts[2]
    header_lines = [l.decode() for l in req_lines[1:]]
    headers = dict([h.split(': ', maxsplit=1) for h in header_lines if len(h) > 2])

    print(f'method: {method}, path: {path}')
    print('headers:')
    print(headers)

    status, headers, body = handler.handle(method, path, headers)
    if len(body) > 0:
        headers['Content-Length'] = len(body)
    headers['Connection'] = 'close'
    headers_list = [b'HTTP/1.1 ' + str(status).encode() + b' ' + STATUS_MAP.get(status, 'SERVER ERROR').encode()]
    headers_list.extend([f'{k}: {v}'.encode() for k, v in headers.items()])
    resp_body = b'\r\n'.join(headers_list) + b'\r\n\r\n'
    if len(body) > 0:
        resp_body += body
    c.sendall(resp_body)

def main(handler):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 8000))  
        s.listen()
        while True:
            c, addr = s.accept()
            server(c, addr, handler)

if __name__ == '__main__':
    main(Handler('D:\\Devel\\html'))