import base64
from flask import Blueprint, request, render_template, Response, current_app
from ..lib.rsa import get_public_key, decrypt

app = Blueprint("controller", __name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/key")
def get_key():
    res = Response(get_public_key(), mimetype="text/plain")
    return res


@app.post("/msg")
def post_msg():
    body = request.get_data()
    msg = base64.urlsafe_b64decode(body)
    plaintext = decrypt(msg).decode()

    current_app.logger.info("MESSAGE RECEIVED:")
    current_app.logger.info(plaintext)

    return {"received": True}
