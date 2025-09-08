# File Transfer Server

This is a simple Python TCP file transfer server built using `socketserver`. It listens for incoming connections, receives a file from the client, and saves it to the server’s file system.

## Features

* Uses Python’s built-in `socketserver` module
* Listens on `localhost:8008` for incoming file uploads
* Receives files from clients via TCP
* Saves received files as `received_file.txt`

## How to Run

1. Clone or download the repository.
2. Run the server script:

```bash
python server.py
```

3. Connect with a TCP client (e.g., `nc` or a Python client) to send a file:

```bash
nc localhost 8008 < somefile.txt
```

4. The server will save the uploaded file as `received_file.txt` in the same directory.

## Notes

* The server currently saves all uploads as `received_file.txt`, overwriting the previous file.
* You can extend the code to include:

  * File name transmission (so each upload keeps its original name)
  * Handling larger files by receiving data in chunks
  * Supporting multiple clients using `ThreadingTCPServer`
