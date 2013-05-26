def is_local():

    import os

    # Distinguish local versus deployed environments
    return os.environ['SERVER_SOFTWARE'].startswith('Development')


def get_request():

    import webapp2

    return webapp2.get_request()


def is_pjax_request():

    import webapp2

    request = webapp2.get_request()
    return 'HTTP_X_PJAX' in request.headers.environ


def pjaxify_response(response):

    # Ensure the pjax url param is included to avoid the browser caching wrong response
    if is_pjax_request():
        response.location = add_url_params(response.location, {'pjax': '#content'})

    return response


def add_url_params(url, params={}):

    import urllib
    import urlparse

    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urllib.urlencode(query)

    return urlparse.urlunparse(url_parts)


def get_full_url(request_handler, path):
    """Return the full url from the provided request handler and path."""

    from urlparse import urlparse

    pr = urlparse(request_handler.request.url)

    return '%s://%s%s' % (pr.scheme, pr.netloc, path)


def split_sentences(text):
    # TODO: Make this non-shite

    return text.split('.')[0].split('!')[0]


def get_abstract(text, length=50):

    return split_sentences(text)[0].replace('<p>', '')[:length]