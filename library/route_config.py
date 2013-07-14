from library import utils


class RouteConfig:

    def __init__(self, name, url=None, route_template=None, jinja_template=None, handler='handlers.static.Handler',
                 cachable=True, requires_signin=False, requires_oauth=False, is_default_redirect_after_signin=False,
                 show_nav=False, nav_title=None):

        self.name = name
        self.url = url or '/' + name
        self.route_template = route_template or self.url
        self.jinja_template = jinja_template or name + '.html'
        self.handler = handler
        self.cachable = cachable
        self.requires_signin = requires_signin
        self.requires_oauth = requires_oauth
        self.is_default_redirect_after_signin = is_default_redirect_after_signin
        self.show_nav = show_nav
        self.nav_title = nav_title


class RouteConfigs(list):

    def __init__(self, *args, **kwargs):
        super(RouteConfigs, self).__init__(*args, **kwargs)

    def get(self, name=None):

        name = name or utils.get_request().route.name
        for route_config in self:
            if route_config.name == name:
                return route_config

        return None

    def get_default_redirect_after_signin(self):

        for route_config in self:
            if route_config.is_default_redirect_after_signin:
                return route_config

        # None specified, so return first route that requires auth
        for route_config in self:
            if route_config.requires_signin:
                return route_config

        return None

    def add(self, route_config):

        if isinstance(route_config, RouteConfig):
            self.append(route_config)
        elif isinstance(route_config, list):
            self.extend(route_config)
