import Crypto.Random.random
from datetime import datetime


def get_synchronizer_token():
    """
    server saves this value
    client gets this value in post form
    when client submits form this token is sent back to server
    server confirm if they match

    if they do not match, log ip attempt

    attacker must guess this value

    token is generated for every form
    """

    from secrets import token_hex
    t = token_hex(256)
    return t
    # print(token_hex(256))
    # r = Crypto.Random.get_random_bytes(256)
    # print(r)
    # return r

def get_encrypted_token():
    """
    server saves key which was used to encrypt this token
    client gets this value in post form
    when client submits form this token is sent back to server
    server confirm if they match and if timestamp is recent

    if they do not match, log ip attempt

    attacker must guess this value

    token is generated for every form

    allows timeout control
    """

    now = datetime.now()  # current date and time
    date_time = now.strftime("%m/%d/%Y_%H:%M:%S:%S")
    print(date_time)

def get_double_submitted_cookie():
    """
    same cookie in form and in cookies
    client send cookie and form

    additional check if they match with server side

    """

def get_captcha():
    """"""

def main():
    # ovo dodaj u formu
    t = get_synchronizer_token()
    print(t)
    print()

    get_encrypted_token()

if __name__ == '__main__':
    main()
