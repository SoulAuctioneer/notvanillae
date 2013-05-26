Not VanillAE
============

The finest web ingredients, blended into a scrumptious boilerplate for Google App Engine.

__Responsive Client__  
HTML5 Boilerplate, Modernizr, Twitter Bootstrap, PJAX.js, socialite.js, and sticky footer, seamlessly blended and buttery smooth.

__Simpler Server__  
A home-made special sauce of decorators and wrappers for Jinja2, OAuth and Google Data API simplifies templating, routing and user sign in.

__Fast__  
Client and server are liberally sprinkled with smart caching treats to keep your site fast and your GAE costs down.

Who's This For?
---------------
Anyone who wants a rapid setup on Google App Engine, using pre-built starter code that merges high-quality boilerplate, frameworks and clever stuff from the community.


Who's This Not For?
-------------------
- You're not using Google App Engine
- You're building a large app that would benefit from a full MVC framework such as Django
- You don't want some random lunatic deciding what is the 'best' tech for your app


What's In It?
-------------
Although VanillAE incorporates a lot of great stuff, I haven't just thrown in everything and the kitchen sink. 
Each component performs a specific useful function that you *probably* want, and does it better than you (easily) could without it. 
Each component is used in the starter site bundled with VanillAE.
If for some reason you don't want a particular component, it's easy to remove.

- [Twitter Bootstrap](http://twitter.github.io/bootstrap/)
- [HTML5 Boilerplate](http://html5boilerplate.com/)
- [Modernizr](http://modernizr.com)
- [Font Awesome](http://fontawesome.io/")
- [PJAX.js](http://pjax.heroku.com/)
- [socialite.js](http://socialitejs.com/)
- [Sticky Footer](http://twitter.github.io/bootstrap/examples/sticky-footer-navbar.html)
- [Jinja2](http://jinja.pocoo.org/docs/)
- [Google APIs](https://developers.google.com/api-client-library/python/start/get_started)
- [Google Users API](https://developers.google.com/appengine/docs/python/users/)


Installation
------------

#### Prerequisites

- [Python 2.7](http://www.python.org/getit/releases/2.7/).
Mac OS X 10.7 Lion users already have Python 2.7 installed.
- [The App Engine SDK for Python](https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python). 
Run the installer if appropriate for your platform, or extract the zip file in a convenient place.

#### Creating a Google App Engine instance

You'll need to host your app on an instance of Google App Engine:
 1. Go to http://appengine.google.com.
 2. Click Create Application and create a public Google App Engine instance hosted on appspot.com.
 3. Give the application an Application Identifier and select Google Accounts users. You'll need the application identifier later to configure Not VanillAE.

#### Getting the code

- __The proper way__: Clone (or fork and clone) this repository
 `git clone https://github.com/SoulAuctioneer/NotVanillAE.git`
- __The easy way__: [Download the zip](https://github.com/SoulAuctioneer/NotVanillAE/archive/master.zip) and extract it.

#### Configuring the app

- Edit `app.yaml` and change the `application` value to the Application Identifier you specified on appspot.com.
- Edit `settings.py` and change `app_title`, `urls`, `oauth` and `google_analytics`.

#### Deploying the app

- Run the following command from a prompt: `appcfg.py update notvanillae/` or click Deploy in Google App Engine Launcher.
- Enter your Google username and password at the prompts.

You can now see your application running on App Engine. If you set up a free appspot.com domain name, the URL for your website begins with your application ID:

http://your-app-id.appspot.com

Congratulations!


Customising Your App
--------------------

- Add __templates__ to the `templates` directory, using `_template.html` for an example.
- Configure __routes__ in `routes.py`, using the examples to get started.
- Add __handlers__ for non-static routes. 
  Generally you will want to __decorate__ your handlers with `@decorators.checks_auth` and `@decorators.sends_response`
- __PJAX__ any internal links by adding a `data-pjax` attribute to your link tags, i.e. `<a href="..." data-pjax>...</a>`
- Add custom __CSS__ to `/assets/css/main.css`
- Add custom __JavaScript__ to `/assets/js/main.js`


Author
------
[Ash Eldritch](http://www.linkedin.com.tw/eldritch)
@ PajamaNinja http://www.pajamaninja.com/


Licenses
--------

Copyright (c) 2013 Ash Eldritch, PajamaNinja / www.pajamaninja.com

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License
