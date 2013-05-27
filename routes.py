from library import utils


class RouteConfig:

    def __init__(self, name, url, route_template=None, jinja_template=None, handler='handlers.static.Handler',
                 cachable=True, requires_auth=False, is_default_redirect_after_signin=False,
                 show_nav=False, nav_title=None):

        self.name = name
        self.url = url
        self.route_template = route_template or url
        self.jinja_template = jinja_template or name
        self.handler = handler
        self.cachable = cachable
        self.requires_auth = requires_auth
        self.is_default_redirect_after_signin = is_default_redirect_after_signin
        self.show_nav = show_nav
        self.nav_title = nav_title


# Routes
route_configs = [
    RouteConfig('intro', '/', is_default_redirect_after_signin=True, show_nav=True, nav_title='Intro'),
    RouteConfig('docs', '/docs', show_nav=True, nav_title='Docs'),
    RouteConfig('signin', '/signin', cachable=False, nav_title='Sign In'),
    RouteConfig('signin_notice', '/signin_notice', cachable=False)
]


def get(name):
    for route_config in route_configs:
        if route_config.name == name:
            return route_config

    return None


def get_current():

    return get(utils.get_request().route.name)


def get_default_redirect_after_signin():

    for route_config in route_configs:
        if route_config.is_default_redirect_after_signin:
            return route_config

    # None specified, so return first route that requires auth
    for route_config in route_configs:
        if route_config.requires_auth:
            return route_config

    return None