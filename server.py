import socketserver

class FileTransferHandler(socketserver.BaseRequestHandler):
    def handle(self):
        file_data = self.request.recv(4096)

        with open('received_file.txt', 'wb') as f:
            f.write(file_data)

server = socketserver.TCPServer(('localhost', 8008), FileTransferHandler)
server.serve_forever()
