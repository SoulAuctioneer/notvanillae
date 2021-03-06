from google.appengine.api import memcache
import os
import webapp2
import pickle
import functools
import hashlib

from library import users
import settings
import routes
import utils


def sends_response(method):

    def _send_response(request_handler, *args, **kwargs):

        # Always call method
        retval = method(request_handler, *args, **kwargs)

        # Handy stuff
        headers = request_handler.response.headers
        is_redirect = type(retval) is webapp2.Response and retval.status_int == 302

        # Browser cache control: set appropriate response headers
        if routes.configs.get().cachable and settings.cache.browser_lifetime is not None:
            # Ensure CDNs will cache static output
            headers['Cache-Control'] = 'public, max-age={max_age}'.format(max_age=settings.cache.browser_lifetime)
        else:
            # Ensure no caching
            headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            headers['Pragma'] = 'no-cache'
            headers['Expires'] = '0'

        # Ensure http can call https
        headers['Access-Control-Allow-Origin'] = settings.urls.canonical

        if is_redirect:
            # If redirecting, ensure the pjax url param is included to avoid the browser caching wrong response
            return utils.pjaxify_response(retval)
        else:
            # Write calling method's return value to response body if not a redirect
            return request_handler.response.out.write(retval)

    return _send_response


def checks_signin(method):
    """
    Verifies that the user is signed in if required in route config
    :param method: Decorated method
    :return: Result of executing decorated method, or redirect if not signed in
    """

    def _check_signin(request_handler, *args, **kwargs):

       # If signin is required, verify signin and bail if not
        if routes.configs.get().requires_signin and not users.is_signed_in():
            return request_handler.redirect('/signin?origin=' + request_handler.request.path)

        # All clear, call our decorated method
        return method(request_handler, *args, **kwargs)

    return _check_signin


def checks_oauth(method):
    """ Verifies oauth if required in route config"""

    def _check_oauth(request_handler, *args, **kwargs):

        # If auth is required and scope is configured, verify auth and bail if not
        if routes.configs.get().requires_oauth:
            retval = users.verify_oauth(request_handler)

            # Bail if auth sends back a redirect
            if type(retval) is webapp2.Response and retval.status_int == 302:
                retval = utils.pjaxify_response(retval)
                return retval

        # All clear, call our decorated method
        return method(request_handler, *args, **kwargs)

    return _check_oauth


def cached(lifetime=settings.cache.default_lifetime, extra_key=None):

    def _cached(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            # Resolve lifetime if it's a function
            resolved_lifetime = lifetime(*args) if hasattr(lifetime, '__call__') else lifetime

            # Return cached version if allowed and available
            if resolved_lifetime is not None:

                # Hash function args for cache key
                items = kwargs.items()
                items.sort()
                hashable_args = (args, tuple(items))
                args_key = hashlib.md5(pickle.dumps(hashable_args)).hexdigest()

                # Generate unique cache key
                cache_key = '{0}-{1}-{2}-{3}'.format(
                    func.__module__,
                    func.__name__,
                    args_key,
                    extra_key() if hasattr(extra_key, '__call__') else extra_key
                )

                result = memcache.get(cache_key)
                if result is not None:
                    return result

            # Generate output
            result = func(*args, **kwargs)

            # Cache output if allowed
            if resolved_lifetime is not None and result is not None:
                memcache.set(cache_key, result, resolved_lifetime)

            return result

        return wrapper

    return _cached
