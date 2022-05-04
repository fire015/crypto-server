import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def get_keys_dir():
    return os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + "/../keys")


def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    public_key = private_key.public_key()

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    dir = get_keys_dir()

    with open(dir + "/private.txt", "wb") as f:
        f.write(private_pem)

    with open(dir + "/public.txt", "wb") as f:
        f.write(public_pem)


def get_public_key():
    file = os.path.join(get_keys_dir(), "public.txt")

    with open(file, "rb") as f:
        key = f.read()

    return key


def get_private_key():
    file = os.path.join(get_keys_dir(), "private.txt")

    with open(file, "rb") as f:
        key = f.read()

    return key


def decrypt(msg):
    private_key = serialization.load_pem_private_key(get_private_key(), password=None)

    plaintext = private_key.decrypt(
        msg,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    return plaintext
