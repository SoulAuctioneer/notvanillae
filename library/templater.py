#!/usr/bin/env python

from google.appengine.api import memcache
import jinja2
import pickle

import users
import settings
import decorators


# Initialize jinja
jinja_environment = jinja2.Environment(
    autoescape=True,
    loader=jinja2.FileSystemLoader(settings.path_templates),
    bytecode_cache=jinja2.MemcachedBytecodeCache(memcache, prefix='jinja2/bytecode/', timeout=settings.cache.jinja_bytecode_timeout)
)


def cache_lifetime(template_name, template_values, is_pjax):

    return settings.cache.template_lifetime \
        if template_name in settings.routes and settings.routes[template_name].cachable \
        else None


@decorators.cached(lifetime=cache_lifetime)
def write(template_name, template_values, is_pjax):

    # Render the output
    template_values = add_template_values(is_pjax, template_values)
    output = render(template_name, template_values)

    return output


def render(template_name, template_values):

    template = jinja_environment.get_template(template_name + '.html')
    return template.render(template_values)


def add_template_values(is_pjax, template_values):

    # Grab standard template values
    if users.is_logged_in():
        template_values['nickname'] = users.get_current_user().nickname()
        template_values['auth_url'] = users.create_logout_url()
    else:
        template_values['nickname'] = None
        template_values['auth_url'] = users.create_login_url()

    # Make configuration settings available to templates
    template_values['settings'] = settings

    # Grab URL constants
    template_values['urls'] = {route_name: route.url for route_name, route in settings.routes.iteritems()}
    template_values['urls']['canonical'] = settings.url_canonical
    template_values['urls']['canonical_secure'] = settings.url_canonical_secure

    # Get app title
    template_values['app_title'] = settings.app_title

    # Identify PJAX requests
    template_values['is_pjax'] = is_pjax

    # Identify local versus deployed
    template_values['is_local'] = settings.is_local

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