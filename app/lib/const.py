import os


_ = os.getenv

APP_HOST = _('APP_HOST', '0.0.0.0')
APP_PORT = int(_('APP_PORT', 8000))
ES_HOST = _('ES_HOST', '0.0.0.0:9200')
ES_INDEX = _('ES_INDEX')
