.. _controller-user_sess:

User Session Controller
=======================

The module offers *add* and *get* functions for user session info.

Controller can save a session information into a database. That data
consists of a user's token and a period in which it is valid in form of
start date and expiry timer.

Once saved, that data can be retrieved by sending the desired user token
to the controller which then returns the desired expiry time and session start,
if an expiry time and session start satisfying the said input data exists.

.. automodule:: src_django.api.controller.user_sess
   :members:
   :undoc-members:
   :show-inheritance:
