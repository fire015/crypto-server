from crypto_server.lib.rsa import generate_keys, get_keys_dir

generate_keys()

print(f"Keys written to {get_keys_dir()}")
