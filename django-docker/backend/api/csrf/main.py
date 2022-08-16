from secrets import token_hex


def get_synchronizer_token():
    """
    Server saves this value.
    Client gets this value in post form.
    When the client submits form, this token is sent back to the server.
    Server confirms if they match.
    If they do not match, ip attempt is logged.
    Token is generated for every form.
    """
    return token_hex(256)
