#!/usr/bin/env python

import webapp2
import routes
from library import users, decorators


class Handler(webapp2.RequestHandler):

    @decorators.sends_response
    def get(self):

        # Here we just delegate sign in to Google Accounts.
        # If you want to handle it yourself, change here and in library.users module

        signedin_landing_url = self.request.get('origin') or routes.configs.get_default_redirect_after_signin().url

        if users.is_signed_in():
            self.redirect(signedin_landing_url)
        else:
            self.redirect(users.create_google_signin_url(signedin_landing_url))
