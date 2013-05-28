#!/usr/bin/env python

import webapp2
import routes
from library import templater, users, decorators


class Handler(webapp2.RequestHandler):

    @decorators.sends_response
    def get(self):

        if not users.is_logged_in():

            # If the user is not logged in, we show an explanation and a login url
            template_values = {
                'authorize_url': users.create_login_url(self.request.get('origin'))
            }
            return templater.write(template_values=template_values)

        else:

            # If the user is logged in, we assume they've seen the explanation page before
            # so we check for oauth creds and redirect to presentation or auth request as appropriate
            return self.redirect(self.get_oath_redirect_url())

    @users.decorator.oauth_aware
    def get_oath_redirect_url(self):

        return routes.get_default_redirect_after_signin().url \
            if users.decorator.has_credentials() \
            else users.decorator.authorize_url()
