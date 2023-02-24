Middleware
===========

Middlewares are used to preprocess incoming requests. A group of requests
can share the same condition to be considered valid. If the validation fails
in the middleware, the request will not be forwarder to the view. Instead, a
false status response will be sent.


Content
-------

.. toctree::
    :maxdepth: 1

    beyond_verifier
    session