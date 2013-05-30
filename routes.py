from library.route_config import RouteConfig, RouteConfigs


# Route configuration
# TODO: Add your own routes here
configs = RouteConfigs([

    RouteConfig('intro', '/', is_default_redirect_after_signin=True, show_nav=True, nav_title='Intro'),

    RouteConfig('docs', '/docs', show_nav=True, nav_title='Docs'),

    RouteConfig('banoffipie', '/banoffipie', show_nav=True, nav_title='Secret Banoffi Pie', requires_signin=True),

    # NOTE: Leave the routes below if you want user authentication and oauth.

    RouteConfig('signin', '/signin', handler='handlers.signin.Handler', cachable=False, nav_title='Sign In'),

    RouteConfig('signin_notice', '/signin_notice', cachable=False),

    RouteConfig('authorize', '/authorize', handler='handlers.authorize.Handler', requires_signin=True, cachable=False),
])
