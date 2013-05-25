#!/usr/bin/env python

import webapp2
from library import templater, decorators, utils

class Handler(webapp2.RequestHandler):

    @decorators.check_auth
    @decorators.send_response
    def get(self):

        # Write template
        # TODO: This currently assumes route name is same as template name
        return templater.write(self.request.route.name, {}, utils.is_pjax(self.request))
