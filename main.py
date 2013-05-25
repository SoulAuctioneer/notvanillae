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

# Insert local directories into path
for code_path in settings.code_paths:
    sys.path.insert(0, code_path)

from library import users

# Initialize web app with routes and handlers and jazz hands
app = webapp2.WSGIApplication(debug=not settings.is_local and not settings.force_dev)
for name, route in settings.routes.iteritems():
    app.router.add(webapp2.Route(route.template, handler=route.handler, name=name))
app.router.add(webapp2.Route(users.decorator.callback_path, handler=users.decorator.callback_handler()))
