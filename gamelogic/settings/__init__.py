"""
This uses a systems hostname to trigger which settings file to load.

If you need to temporarily override which settings file to use, you can do this
on the command line, e.g.::

    ./manage.py runserver --settings=settings.other

To determine the hostname, run `hostname` from the server's command line.
"""
import socket

hostname = socket.gethostname()

if hostname == 'web28.webfaction.com':
    from production import *
else:
    from local import *

