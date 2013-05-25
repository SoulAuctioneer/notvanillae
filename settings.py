import os
from library.dotdict import DotDict

# Distinguish local versus deployed environments
is_local = os.environ['SERVER_SOFTWARE'].startswith('Development')

# Force dev mode even on deployed app. Should be true only when debugging. Caching and error reporting use this setting
force_dev = False

# App title, used for page title and social sharing title
app_title = 'AppEngine Boilerplate by Ash Eldritch'

# Paths to templates and code. Add any new directories to code_paths
path_base = os.path.dirname(os.path.abspath(__file__))
path_templates = os.path.join(path_base, 'templates')
code_paths = [os.path.join(path_base, endpoint) for endpoint in [
    'handlers',
    'library',
    'external',
    'external/googleapi'
]]

# URLs -
url_canonical = 'http://localhost:8080' if is_local else 'http://yourshow.pajamaninja.com'
url_canonical_secure = 'http://localhost:8080' if is_local else 'https://yourshow.pajamaninja.com'

# Routes
# TODO: Make into a class RouteConfig. Add jinja2 template property, as currently assuming same as route
routes = DotDict({
    'intro': DotDict({'url': '/', 'template': '/', 'handler': 'handlers.static.Handler', 'cachable': True}),
    'signin': DotDict({'url': '/signin', 'template': '/signin', 'handler': 'handlers.signin.Handler', 'cachable': False, 'auth_required': False}),
    'signin_notice': DotDict({'url': '/signin_notice', 'template': '/signin_notice', 'handler': 'handlers.static.Handler', 'cachable': False, 'auth_required': False}),
    'blog': DotDict({'url': '/blog', 'template': '/blog', 'handler': 'handlers.blog.Handler', 'cachable': True, 'auth_required': False}),
    'blog_post': DotDict({'url': '/blog/post/%s/%s', 'template': '/blog/post/<post_id>/<post_slug>', 'handler': 'handlers.blog.Handler', 'cachable': True, 'auth_required': False}),
    'blog_tagged': DotDict({'url': '/blog/tagged/%s', 'template': '/blog/tagged/<tag>', 'handler': 'handlers.blog.Handler', 'cachable': True, 'auth_required': False}),
})

# Google Data API OAuth Credentials, as per https://code.google.com/apis/console/?pli=1#project:909315780380:access
oauth = DotDict({
    'client_id': '909315780380.apps.googleusercontent.com',
    'client_secret': 'euQh7F-17Y0mc9mom8NJFheh',
    'scope': [
        #'https://www.googleapis.com/auth/drive.readonly',
        #'https://www.googleapis.com/auth/drive',
        #'https://www.googleapis.com/auth/drive.apps.readonly',
        #'https://www.googleapis.com/auth/drive.metadata.readonly',
        #'https://www.googleapis.com/auth/drive.file',
        #'https://www.googleapis.com/auth/drive.scripts',
        #'https://www.googleapis.com/auth/userinfo.profile',
        #'https://www.googleapis.com/auth/glass.timeline ',
    ]
})

# Google Analytics
ga = DotDict({
    'enabled': False,
    'id': '',
    'domain': ''
})

# Global caching toggle. Allow caching if environment is not local and we're not forcing dev mode
cache_enabled = not is_local and not force_dev

# Specific caching settings
cache = DotDict({
    'default_lifetime': None if not cache_enabled else 120,
    'template_lifetime': None if not cache_enabled else 18000,
    'browser_lifetime': None if not cache_enabled else 691200,
    'jinja_bytecode_lifetime': None if not cache_enabled else 3600
})
