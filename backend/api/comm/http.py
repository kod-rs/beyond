def get_empty_response_template():
    response = {
        "auth": {
            "status": False,
            "access-token": "",
            "refresh-token": ""
        },
        "payload": {
        },
        "debug": {
        }
    }
    return response
