#server.py
from .main import edit
import socket
import threading
import asyncio
import websockets
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime
__all__ = ["run_server", "run_ws", "run_http"]
class _packet:
    @staticmethod
    def encode(text):
        s = str(text)
        return f"{len(s)}|{s}".encode()
    @staticmethod
    def decode(raw):
        if isinstance(raw, bytes):
            raw = raw.decode(errors="ignore")
        if "|" not in raw:
            return None
        l, data = raw.split("|", 1)
        return data
class _router:
    def __init__(self):
        self.routes = {}
    def add(self, command, func):
        self.routes[str(command)] = func
    def route(self, text):
        parts = str(text).split()
        if not parts:
            return "ERR"
        cmd = parts[0]
        if cmd in self.routes:
            return self.routes[cmd](text)
        return "NO_ROUTE"
class _client:
    def __init__(self, host="127.0.0.1", port=5050):
        self.host = host
        self.port = int(port)
        self.addr = (self.host, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cserver = self.addr[0]
        self.cport = self.addr[1]
        self.cname = edit.join(edit.join(self.cserver, ":"), self.cport)
    def connect(self):
        self.sock.connect(self.addr)
    def send(self, text):
        self.sock.sendall(_packet.encode(text))
    def recv(self, n=4096):
        return _packet.decode(self.sock.recv(int(n)))
    def close(self):
        self.sock.close()
class _wsserver:
    def __init__(self, host="127.0.0.1", port=8765):
        self.host = host
        self.port = int(port)
    async def _log(self, msg):
        t = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[WS {t}] {msg}")
    async def _handler(self, ws, path):
        await self._log("connect")
        try:
            async for message in ws:
                await self._log(f"recv {message}")
                await ws.send("OK")
        except:
            pass
        await self._log("disconnect")
    async def start(self):
        async with websockets.serve(self._handler, self.host, self.port):
            await self._log("running")
            await asyncio.Future()
class _httphandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"HTTP SERVER\nPath: {self.path}\nTime: {datetime.datetime.now()}"
        b = body.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", len(b))
        self.end_headers()
        self.wfile.write(b)
class _httpserver:
    def __init__(self, host="127.0.0.1", port=8080):
        self.host = host
        self.port = int(port)
        self.server = HTTPServer((host, port), _httphandler)
    def start(self):
        print(f"[HTTP] {self.host}:{self.port}")
        self.server.serve_forever()
    def stop(self):
        self.server.shutdown()
class _server:
    def __init__(self, host="127.0.0.1", port=5050):
        self.host = host
        self.port = int(port)
        self.addr = (host, port)
        self.router = _router()
        self.router.add("ping", lambda t: "pong")
        self.router.add("echo", lambda t: t)
    def _log(self, m):
        t = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[TCP {t}] {m}")
    def _handle(self, conn, addr):
        self._log(f"connect {addr}")
        try:
            while True:
                raw = conn.recv(1024)
                if not raw:
                    break
                msg = _packet.decode(raw)
                out = self.router.route(msg)
                conn.sendall(_packet.encode(out))
        except:
            pass
        self._log(f"disconnect {addr}")
        conn.close()
    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(self.addr)
        s.listen()
        self._log(f"running {self.host}:{self.port}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=self._handle, args=(conn, addr), daemon=True).start()
def run_server(host="127.0.0.1", port=5050):
    srv = _server(host, port)
    srv.start()
def run_ws(host="127.0.0.1", port=8765):
    ws = _wsserver(host, port)
    asyncio.run(ws.start())
def run_http(host="127.0.0.1", port=8080):
    http = _httpserver(host, port)
    http.start()