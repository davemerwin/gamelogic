import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append('/home/tbiedu/webapps/gamelogic/gamelogic/gamelogic/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'gamelogic.settings'

import site
site.addsitedir('/home/tbiedu/.virtualenvs/gamelogic/lib/python2.6/site-packages')

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()