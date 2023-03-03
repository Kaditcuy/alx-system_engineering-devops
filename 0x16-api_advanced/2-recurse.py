#!/usr/bin/python3

"""
queries the Reddit API and returns the titles of a given
subreddit. If an invalid subreddit is given, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results
    are found for the given subreddit, the function returns None.
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {'User-Agent': 'something'}

    params = {'limit': 100}

    if after:  # for pagination
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()['data']

    hot_list.extend([post['data']['title'] for post in data['children']])

    after = data['after']

    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
