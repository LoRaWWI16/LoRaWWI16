import sys

sys.path.insert(0, "/var/www/Lora")

import bottle
from template import app as application
application = bottle.default_app()