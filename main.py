#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
import webapp2
import settings
import routes
from library import utils

# Insert local directories into path
for code_path in settings.code_paths:
    sys.path.insert(0, code_path)

from library import users

# Initialize web app with routes and handlers and jazz hands
app = webapp2.WSGIApplication(debug=utils.is_local() or settings.force_dev)
for route_config in routes.configs:
    app.router.add(webapp2.Route(route_config.route_template, handler=route_config.handler, name=route_config.name))
app.router.add(webapp2.Route(users.oauth_decorator.callback_path, handler=users.oauth_decorator.callback_handler()))
