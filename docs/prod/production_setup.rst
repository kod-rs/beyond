General
=======

Project's frontend is served through *Nginx*, which communicates with *Django*
backend and *Keycloak* service to display buildings. Required tools are node.js, 
Python (Django) and Nginx.

Django
=======

Django desn't require any special treatment as it is quite ready for production
with a few adjustments. However, some Django settings are not acceptable in 
production environments such as ``debug = True`` flag which **must** be fixed 
accordingly. Description of all checks can be found here_.

.. _here: https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

Project defaults to run in development environment instead of production.
At this stage it is required to change Django internal settings to fetch
info from ``prod.py`` instead of ``dev.py``. This is done by changing
``manage.py``, ``asgi.py``, ``wsgi.py`` and src_django.settings ``__init__.py``
like shown below.

.. code-block:: python

  'src_django.settings.dev' -> 'src_django.settings.prod'

It is also worth noting that for production purposes it is recommended to have a
secret key in separate file. In our case it is named ``secret_key.txt`` and 
should be placed in home directory.

Nginx
======

Production build is being statically served via *Nginx*. After installation 
*Nginx* is supposed to work out of the box but still requires little bit of 
tweaks. At this stage, if you go to your servers IP address, it should display 
message like this:

	**Welcome to nginx!**
	If you see this page, web server is successfuly...


If there is an error it is strongly recommended to ask ChatGPT to help resolve
any potential issues. First and foremost, using npm create production build for 
*React* frontend.

::

  $ npm run build

As Nginx serves static files copy build folder to some location (which defaults 
to \/var\/www\/html). Of course it is possible to create separate folder for 
each project and keep generated assets here, but for simplicity reasons we'll 
keep it in root.
::

  $ sudo cp -r /path/to/beyond/src_front/build/. /var/www/html

Next part revolves around configuring server file (it is located under
``/etc/nginx/sites-available/default``). Firstly, since size of 
packets sent to user via Djagno containing building info will increase 
proportional to number of buildings it is recommended to increase client
packet size. This is done by adding following variable in server config 
file under *server* directive (set it to any number greater than 64M).

:: 

  $ client_max_body_size 128M;

Afterwards, we will set server to proxy any *POST* and *GET* requests
to Django backend which will be running on localhost on port 8000. This step
is performed by adding *proxy_pass* variable to *location* field several times
for each site loaction (e.g. /login).

::

  location /login {
	  proxy_pass http://127.0.0.1:8000;
  }

Every time someone makes changes to server configuraton file it is required
to reload server. This is done by sudo service *service_name* restart.