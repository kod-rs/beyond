from decouple import config

def shortcircuitmiddleware(f):
    """ view decorator, the sole purpose to is 'rename' the function
    '_shortcircuitmiddleware' """
    def _shortcircuitmiddleware(*args, **kwargs):
        return f(*args, **kwargs)
    return _shortcircuitmiddleware

class ShortCircuitMiddleware(object):
    """ Middleware; looks for a view function named '_shortcircuitmiddleware'
    and short-circuits. Relies on the fact that if you return an HttpResponse
    from a view, it will short-circuit other middleware, see:
    https://docs.djangoproject.com/en/dev/topics/http/middleware/#process-request
     """
    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.func_name == "_shortcircuitmiddleware":
            return view_func(request, *view_args, **view_kwargs)
        return None

class DebuggableMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"

    def log(self, payload):
        if self.debug:
            print(payload)

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


def middleware_check_params(vue_interface_cfg,c, given):
    route = c.split(";")[0]
    action = c.split(";")[1]
    # print(f"{route=} {action=} {given=}")


    # print(vue_interface_cfg)
    if route not in vue_interface_cfg:
        # print("route not in vue")
        return False
    r = vue_interface_cfg[route]
    # print("tu")
    # print(r)



    if action not in r:
        return False

    r = r[action]
    print(r)
    return all([given.__contains__(i) for i in r])
