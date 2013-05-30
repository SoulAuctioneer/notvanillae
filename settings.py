import os
from library.dotdict import DotDict
from library import utils
from library.route_config import RouteConfig

# App title, used for page title and social sharing title
# TODO: Update this app title to reflect your own
app_title = 'Not VanillAE'

# URLs
# TODO: Change this to reflect your local and production URLs
urls = DotDict({
    'canonical': 'http://localhost:8080' if utils.is_local() else 'http://notvanillae.appspot.com',
    'canonical_secure': 'http://localhost:8080' if utils.is_local() else 'http://notvanillae.appspot.com'
})

# Google Data API OAuth Credentials
# TODO: Update these to reflect your own scope requirements and credentials at https://code.google.com/apis/console/
oauth = DotDict({
    'client_id': '909315780380-4srs376b72kso2uui8u6qps8joatm0mg.apps.googleusercontent.com',
    'client_secret': 'Ko5HzoC4_3z9EW8-9VAK4o4z',
    'scope': [
        #'https://www.googleapis.com/auth/glass.timeline ',
        #'https://www.googleapis.com/auth/drive.readonly',
        #'https://www.googleapis.com/auth/drive',
        #'https://www.googleapis.com/auth/drive.apps.readonly',
        #'https://www.googleapis.com/auth/drive.metadata.readonly',
        #'https://www.googleapis.com/auth/drive.file',
        #'https://www.googleapis.com/auth/drive.scripts',
        #'https://www.googleapis.com/auth/userinfo.profile',
    ]
})

# Google Analytics
# TODO: Update these to reflect your own Google Analytics identifiers
google_analytics = DotDict({
    'enabled': not utils.is_local(),
    'id': '',
    'domain': ''
})

# Force dev mode even on deployed app. Should be true only when debugging. Caching and error reporting use this setting
force_dev = False

# Paths to templates and code. Add any new directories to code_paths
path_base = os.path.dirname(os.path.abspath(__file__))
path_templates = os.path.join(path_base, 'templates')
code_paths = [os.path.join(path_base, endpoint) for endpoint in [
    'handlers',
    'library',
    'external',
    'external/googleapi'
]]

# Global caching toggle. Allow caching if environment is not local and we're not forcing dev mode
cache_enabled = not utils.is_local() and not force_dev

# Specific caching settings
cache = DotDict({
    'default_lifetime': None if not cache_enabled else 120,
    'template_lifetime': None if not cache_enabled else 18000,
    'browser_lifetime': None if not cache_enabled else 691200,
    'jinja_bytecode_lifetime': None if not cache_enabled else 3600
})
