from library import utils


class RouteConfig:

    def __init__(self, name, url, route_template=None, jinja_template=None, handler='handlers.static.Handler',
                 cachable=True, requires_signin=False, requires_oauth=False, is_default_redirect_after_signin=False,
                 show_nav=False, nav_title=None):

        self.name = name
        self.url = url
        self.route_template = route_template or url
        self.jinja_template = jinja_template or name + '.html'
        self.handler = handler
        self.cachable = cachable
        self.requires_signin = requires_signin
        self.requires_oauth = requires_oauth
        self.is_default_redirect_after_signin = is_default_redirect_after_signin
        self.show_nav = show_nav
        self.nav_title = nav_title


# Routes
# TODO: Add your own routes here.
route_configs = [
    RouteConfig('intro', '/', is_default_redirect_after_signin=True, show_nav=True, nav_title='Intro'),
    RouteConfig('docs', '/docs', show_nav=True, nav_title='Docs'),
    RouteConfig('banoffipie', '/banoffipie', show_nav=True, nav_title='Secret Banoffi Pie', requires_signin=True, requires_oauth=True),
    # NOTE: Leave the routes below if you want user authentication and oauth.
    RouteConfig('signin', '/signin', handler='handlers.signin.Handler', cachable=False, nav_title='Sign In'),
    RouteConfig('signin_notice', '/signin_notice', cachable=False),
    RouteConfig('authorize', '/authorize', handler='handlers.authorize.Handler', requires_signin=True, cachable=False),
]


def get(name=None):

    name = name or utils.get_request().route.name
    for route_config in route_configs:
        if route_config.name == name:
            return route_config

    return None


def get_default_redirect_after_signin():

    for route_config in route_configs:
        if route_config.is_default_redirect_after_signin:
            return route_config

    # None specified, so return first route that requires auth
    for route_config in route_configs:
        if route_config.requires_oauth:
            return route_config

    return None