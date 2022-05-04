# Crypto server

This is a POC using [Pyodide](https://pyodide.org/) to execute Python code in the browser to encrypt a message client-side and decrypt it server-side.

## How it works

Using the same [cryptography](https://cryptography.io/) Python package on the client and server, we first encrypt a message client-side using the generated RSA public key (`GET /key`). The encrypted message is sent to the server via the `POST /msg` endpoint and is decrypted using the RSA private key.

```
127.0.0.1 - - [04/May/2022 16:15:33] "GET /key HTTP/1.1" 200 -
[2022-05-04 16:15:34,209] INFO in controller: MESSAGE RECEIVED:
[2022-05-04 16:15:34,209] INFO in controller: This is my super secret message!
127.0.0.1 - - [04/May/2022 16:15:34] "POST /msg HTTP/1.1" 200 -
```

## Setup

Tested with Python 3.8.

```
pip install -r requirements.txt

python generate_keys.py

python server.py
```

Open Chrome to http://localhost:3000/