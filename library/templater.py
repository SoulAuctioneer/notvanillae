#!/usr/bin/env python

from google.appengine.api import memcache
import jinja2

import settings
import routes
import users
import decorators
import utils
from jinja2htmlcompress import jinja2htmlcompress


# Initialize jinja
jinja_environment = jinja2.Environment(
    autoescape=True,
    loader=jinja2.FileSystemLoader(settings.path_templates),
    bytecode_cache=jinja2.MemcachedBytecodeCache(memcache, prefix='jinja2/bytecode/', timeout=settings.cache.jinja_bytecode_timeout)
)

# Add html compressor
if settings.compress_html:
    jinja_environment.add_extension(jinja2htmlcompress.HTMLCompress)


def cache_lifetime(routeconfig_name=None):

    return settings.cache.template_lifetime if routes.configs.get(routeconfig_name).cachable else None


def template_cachekey(routeconfig_name=None):
    """
    Generates a key that is unique to the given or current RouteConfig and whether the request is a PJAX request
    :param routeconfig_name: Name of RouteConfig. Defaults to the current request's RouteConfig
    :type routeconfig_name: str
    :return: The template filename for the given template name.
    """
    return (routeconfig_name or routes.configs.get().name) + '-' + str(utils.is_pjax_request())


@decorators.cached(lifetime=cache_lifetime, extra_key=template_cachekey)
def write(routeconfig_name=None, template_values={}):
    """
    Renders the template specified in the named RouteConfig, or the current route's RouteConfig if none is given
    :param routeconfig_name: Name of the RouteConfig containing the template name. Defaults to the current request's RouteConfig
    :param template_values: Dictionary of values made available to the template
    :return: Output of the rendered template
    """

    # Render the output
    template_values = add_standard_template_values(template_values)
    output = render(routes.configs.get(routeconfig_name).jinja_template, template_values)

    return output


def render(template_filename, template_values):

    template = jinja_environment.get_template(template_filename)
    return template.render(template_values)


def add_standard_template_values(template_values):

    # Specify base template based on whether this is a pjax request
    template_values['base_template'] = 'base_pjax.html' if utils.is_pjax_request() else 'base.html'

    # Authentication information
    # NOTE: This may fall foul of template output caching if used by routes that allow caching.
    if users.is_signed_in():
        template_values['nickname'] = users.get_current_user().nickname()
        template_values['auth_url'] = users.create_google_signout_url()
    else:
        template_values['nickname'] = None
        template_values['auth_url'] = users.create_google_signin_url()

    # Make configuration settings available to templates
    template_values['settings'] = settings
    template_values['route_configs'] = routes.configs

    # Identify local versus deployed
    template_values['is_local'] = utils.is_local()

    # Set defaults for page title and active nav
    nav_title = routes.configs.get().nav_title
    template_values['title'] =  nav_title + ' - ' + settings.app_title if nav_title else settings.app_title
    template_values['active_nav'] = routes.configs.get().name

    return template_values


def format_datetime(value, format='medium'):

    import time

    if format == 'full':
        format="%a, %d %b %Y %H:%M:%S +0000"
    elif format == 'medium':
        format="%a %d %b %Y"
    elif format == 'small':
        format="%d %b %Y"

    return time.strftime(format, value)

jinja_environment.filters['datetime'] = format_datetime