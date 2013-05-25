from urlparse import urlparse
import webapp2


def is_pjax():

    request = webapp2.get_request()
    return 'HTTP_X_PJAX' in request.headers.environ


def pjaxify_response(response):

    # Ensure the pjax url param is included to avoid the browser caching wrong response
    if is_pjax():
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
    pr = urlparse(request_handler.request.url)
    return '%s://%s%s' % (pr.scheme, pr.netloc, path)


def split_sentences(text):
    # TODO: Make this non-shite

    return text.split('.')[0].split('!')[0]


def get_abstract(text, length=50):

    return split_sentences(text)[0].replace('<p>', '')[:length]