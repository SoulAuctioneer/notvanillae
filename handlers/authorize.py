#!/usr/bin/env python

import webapp2
import routes
from library import templater, users, decorators


class Handler(webapp2.RequestHandler):

    @decorators.checks_signin
    @users.oauth_decorator.oauth_aware
    @decorators.sends_response
    def get(self):

        if users.oauth_decorator.has_credentials():
            authorized_url = self.request.get('origin') or routes.get_default_redirect_after_signin().url
            return self.redirect(authorized_url)
        else:
            template_values = {
                'authorize_url': users.oauth_decorator.authorize_url()
            }
            return templater.write(template_values=template_values)
