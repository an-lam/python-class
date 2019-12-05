import base64

id_password = "aulac:abcd".encode()
auth_key = base64.b64encode(id_password)
print("auth_key: " + str(auth_key))