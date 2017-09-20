#!/usr/bin/python
"""
the twit package is a bear python-twitter adapter
"""
import twitter
import helpers
import config
import time
from dateutil import parser


class API():
    """ contextual twitter api for setting up and tearing down before running functional methods."""

    # intilize
    def __init__(self):
        self.client = twitter.Api(consumer_key=config.twitter_consumer_key,
                                  consumer_secret=config.twitter_consumer_secret,
                                  access_token_key=config.twitter_access_token,
                                  access_token_secret=config.twitter_access_secret)

    # setup
    def __enter__(self):
        return self.client

    # teardown
    def __exit__(self, *args):
        self.client = None


def search(term):
    """ get_recent_tweets_with_search_term returns 100 search results per term """

    with API() as api:
        return api.GetSearch(term=term, count=100, result_type="recent")


def get_tweep(tweep):
    """ gets a twitter user, aka tweep. """
    with API() as api:
        return api.GetUser(tweep)


def check_account_for_new_posts(account, cutoff):
    """ gets a twitter user, aka account. """
    with API() as api:
        posts = []
        timeline = api.GetUserTimeline(
            screen_name=account, count=10, include_rts=False, exclude_replies=True)

        for post in timeline:
            post_time = post.created_at
            now_ts = int(helpers.get_time_now(stringify=True)) - cutoff
            if post_time >= now_ts:
                posts.append(post)

        return posts
