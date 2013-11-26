Not VanillAE
============

The finest web ingredients, blended into a scrumptious boilerplate for Google App Engine.

Sample websites created with Not VanillAE: [SAMA Kitchen](http://www.samakitchen.com), [Superhuman Labs](http://www.superhumanlabs.com), [VitalMedicals](http://www.vitalmedicals.com), [NoJack](http://www.nojackalarm.com), [YourShow](http://yourshow.superhumanlabs.com)

__Responsive Client__  
HTML5 Boilerplate, Twitter Bootstrap, Modernizr, PJAX.js, socialite.js, and sticky footer, seamlessly blended and buttery smooth.

__Simpler Server__  
Webapp2, Jinja2 and Google Service APIs on Python 2.7, all drizzled with home-made decorators and wrappers for lightweight routing, templating and user authentication.

__Fast__  
Liberally sprinkled with smart caching treats, async javascript loading and squished css/javascript to keep your site fast and your GAE costs down.

Who's this for?
---------------
Not VanillAE is great for anyone who wants a rapid setup on Google App Engine, 
using pre-built starter code that merges high-quality boilerplate, frameworks and clever stuff from the community.

This isn't a good fit if:
- You're not using Google App Engine
- You're building a large app that would benefit from a full MVC framework such as Django
- You need a Content Management System (take a look at Django-cms + Google Cloud SQL, or Vosao for Java on GAE)
- You don't want some random lunatic deciding what is the 'best' tech for your app


What's in it?
-------------
Although VanillAE incorporates a lot of great stuff, I haven't just thrown in everything and the kitchen sink. 
Each component performs a specific useful function that you *probably* want, and does it better than you (easily) could without it. 
Each component is used in the starter site bundled with VanillAE.
If for some reason you don't want a particular component, it's easy to remove.

- [Twitter Bootstrap](http://twitter.github.io/bootstrap/)
- [HTML5 Boilerplate](http://html5boilerplate.com/)
- [Modernizr](http://modernizr.com) (disabled by default in favour of html5shim)
- [Font Awesome](http://fontawesome.io/")
- [PJAX.js](http://pjax.heroku.com/)
- [socialite.js](http://socialitejs.com/)
- [Sticky Footer](http://twitter.github.io/bootstrap/examples/sticky-footer-navbar.html)
- [Jinja2](http://jinja.pocoo.org/docs/)
- [Google APIs](https://developers.google.com/api-client-library/python/start/get_started)
- [Google Users API](https://developers.google.com/appengine/docs/python/users/)

Some features provided by other boilerplates are not included. I will be considering these for future versions:
- User preferences and mangagement outside Google accounts
- Sessions
- I18N
- Unit testing
- Form validation

If you need these features you can take a look at
[App Engine Essence](https://github.com/alchemycs/appengine-essence)
or [Google App Engine Boilerplate](https://github.com/ronw23/gae-boilerplate)


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

### Optional

Not VanillAE uses [Grunt](http://gruntjs.com/) to automate css and js minification and concatenation. To install:
 1. Install [Node.js](http://nodejs.org/download/)
 2. Install the Grunt CLI: `npm install -g grunt-cli`
 3. Change to the project's root directory.
 4. Install project dependencies with `npm install`.
 5. Run Grunt with `grunt`.


Customising your app
--------------------

- Add __templates__ to the `templates` directory, using `_template.html` for an example.
- Configure __routes__ in `routes.py`, using the examples to get started.
- Add __handlers__ for non-static routes.
- __Decorate__ your handler methods with `@decorators.checks_auth` and/or `@decorators.sends_response`. A `@cached` decorator is also available.
- __PJAX__ any internal links by adding a `data-pjax` attribute to your link tags, i.e. `<a href="..." data-pjax>...</a>`
- Add custom __CSS__ to `/assets/css/main.css`
- Add custom __JavaScript__ to `/assets/js/main.js`


To do
-----

- Allow app to be deployed without Grunt
- Comment all code
- Score >95% on Google Page Speed.
- Determine a [dependency management strategy](http://bower.io/).
- Integrate option for [user authentication via OpenID](https://developers.google.com/appengine/articles/openid).
- Identify and review [similar](https://github.com/alchemycs/appengine-essence) [boilerplate](https://github.com/coto/gae-boilerplate/) projects for good ideas to incorporate.
- Create more comprehensive customization documentation.


Meta
------
Author: [Ash Eldritch](http://www.linkedin.com.tw/eldritch) @ PajamaNinja http://www.pajamaninja.com/

License: Distributed under the [MIT license](http://opensource.org/licenses/MIT). All dependencies have their own licenses.

[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/382cdd95d5655cd9c0c9d0adabc05614 "githalytics.com")](http://githalytics.com/SoulAuctioneer/notvanillae)
