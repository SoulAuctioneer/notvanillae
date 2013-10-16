from library.route_config import RouteConfig, RouteConfigs


# Route configuration
configs = RouteConfigs([

    RouteConfig('intro', '/', is_default_redirect_after_signin=True, show_nav=False),
    RouteConfig('team', show_nav=True, nav_title='Team'),
    RouteConfig('contact', show_nav=True, nav_title='Contact')

])
