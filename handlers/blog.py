#!/usr/bin/env python

import webapp2
import settings
from library import templater, decorators, utils, tumblr


class Handler(webapp2.RequestHandler):

    @decorators.check_auth
    @decorators.send_response
    def get(self, tag=None, post_id=None, post_slug=None):

        # Get posts, filtering if such args are given
        kwargs = {'limit': 50}
        if tag is not None:
            kwargs['tag'] = tag
        if post_id is not None:
            kwargs['id'] = post_id
        posts = tumblr.get_posts(**kwargs)

        template_data = {
            'posts': posts,
            'tags': tumblr.get_all_tags(),
            'recent_posts': tumblr.get_posts(limit=settings.tumblr.num_recent_posts),
            'tag': tag,
            'filter': 'post_id' if post_id else 'tag' if tag else None
        }

        return templater.write('blog', template_data, utils.is_pjax(self.request))
