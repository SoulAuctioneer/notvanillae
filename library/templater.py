#!/usr/bin/env python

from google.appengine.api import memcache
import jinja2

import settings
import routes
import users
import decorators
import utils


# Initialize jinja
jinja_environment = jinja2.Environment(
    autoescape=True,
    loader=jinja2.FileSystemLoader(settings.path_templates),
    bytecode_cache=jinja2.MemcachedBytecodeCache(memcache, prefix='jinja2/bytecode/', timeout=settings.cache.jinja_bytecode_timeout)
)


def cache_lifetime(template_name=None):

    # Resolve template if not specified
    template_name = template_name or routes.get_current().jinja_template

    return settings.cache.template_lifetime if routes.get(template_name).cachable else None


@decorators.cached(lifetime=cache_lifetime)
def write(template_name=None, template_values={}):

    # Resolve template if not specified
    template_name = template_name or routes.get_current().jinja_template

    # Render the output
    template_values = add_standard_template_values(template_values)
    output = render(template_name, template_values)

    return output


def render(template_name, template_values):

    template = jinja_environment.get_template(template_name + '.html')
    return template.render(template_values)


def add_standard_template_values(template_values):

    # Specify base template based on whether this is a pjax request
    template_values['base_template'] = 'base_pjax.html' if utils.is_pjax_request() else 'base.html'

    # Authentication information
    if users.is_logged_in():
        template_values['nickname'] = users.get_current_user().nickname()
        template_values['auth_url'] = users.create_logout_url()
    else:
        template_values['nickname'] = None
        template_values['auth_url'] = users.create_login_url()

    # Make configuration settings available to templates
    template_values['settings'] = settings
    template_values['route_configs'] = routes.route_configs

    # Identify local versus deployed
    template_values['is_local'] = utils.is_local()

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