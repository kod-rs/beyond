General
=======

Project's frontend is served through *Nginx*, which communicates with *Django*
backend and *Keycloak* service to display buildings. Required tools are node.js, 
Python and Nginx. Bla bla bla

Django
=======

Django desn't require any special treatment as it is quite ready for production
with a few adjustments. Bla bla bla..

Nginx
======

Production build is being statically served via *Nginx*. After installation *Nginx*
is supposed to work out of the box which requires little bit of tweaks.At this 
moment, if you go to your servers IP address, it will look something like this:

|              **Welcome to nginx!**
| If you see this page, web server is successfuly...

If there is an error it is strongly recommended to ask ChatGPT for help to resolve
any potential issues. First and foremost, using npm create production build for 
*React* frontend.

``$ npm run build``

As Nginx serves static files it is recommended to copy build folder to some 
location (e.g. defaults \/var\/www\/html). Of course it is possible to create separate 
folder for each project and keep generated assets here, but for simplicity
reasons it will be in root.

``$ sudo cp -r \/path\/to\/beyond\/src_front\/build\/. \/var\/www\/html``

Next part revolves around configuring Nginx server to proxy `POST` and `GET` 
requests to Django backend. Configuration file is supposed to look something like this:

