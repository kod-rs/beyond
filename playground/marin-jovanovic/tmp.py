jwt = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmk3CwATt01k9kjA86MDM
EWkyTuFCWe72EEFggzs+ErjWipbs4RebYtaY52qnZ0w8ZiUPU/QL3sNZO7T2SOci
nEaAG21JdqBtBcw+8GCTZs72gWqNgXXCO9ZpqHBjQq7eLXYoCC9E3+G6OfAH5kF/
eJl99n1grDdbNjdVnFOvuUgMxwmwjf2Kd2seqpe0LK8Od3Ipu30x28Mg06k1uTcm
umlRS61R3EwLyjbNCTwOmDyIWWGAfat1XL0QZoKicJsuNb841XKF0cJvepcZ2ILS
7+7xP2QOpkajShje/nKQUm8Gvp5zHzpa7XyAk1p/DzgYwVLnfYM0K4eHO6fqDGnV
nQIDAQAB
-----END PUBLIC KEY-----
"""

if isinstance(jwt, str):
    jwt = jwt.encode("utf-8")

print(jwt)
t = b'hello'
t = "hello"
if isinstance(t, bytes):
    encoding = 'utf-8'
    t = t.decode(encoding)
print(t, type(t))

jwt = "b'-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmk3CwATt01k9kjA86MDM\\nEWkyTuFCWe72EEFggzs+ErjWipbs4RebYtaY52qnZ0w8ZiUPU/QL3sNZO7T2SOci\\nnEaAG21JdqBtBcw+8GCTZs72gWqNgXXCO9ZpqHBjQq7eLXYoCC9E3+G6OfAH5kF/\\neJl99n1grDdbNjdVnFOvuUgMxwmwjf2Kd2seqpe0LK8Od3Ipu30x28Mg06k1uTcm\\numlRS61R3EwLyjbNCTwOmDyIWWGAfat1XL0QZoKicJsuNb841XKF0cJvepcZ2ILS\\n7+7xP2QOpkajShje/nKQUm8Gvp5zHzpa7XyAk1p/DzgYwVLnfYM0K4eHO6fqDGnV\\nnQIDAQAB\\n-----END PUBLIC KEY-----\\n'"

jwt = bytes(jwt[2:-1], "utf-8")
print(jwt)
print(type(jwt))

if isinstance(jwt, str):
    jwt = jwt.encode("utf-8")


try:
    signing_input, crypto_segment = jwt.rsplit(b".", 1)
    header_segment, payload_segment = signing_input.split(b".", 1)
except ValueError as err:
    raise DecodeError("Not enough segments") from err