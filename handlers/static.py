#!/usr/bin/env python

import webapp2
from library import templater, decorators


class Handler(webapp2.RequestHandler):

    @decorators.checks_auth
    @decorators.sends_response
    def get(self):

        # Write template
        return templater.write()
