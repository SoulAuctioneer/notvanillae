#!/usr/bin/env python

import webapp2
from library import templater, decorators, utils


class Handler(webapp2.RequestHandler):

    @decorators.checks_signin
    @decorators.checks_oauth
    @decorators.sends_response
    def get(self):

        # Write template configured for current route
        return templater.write()
