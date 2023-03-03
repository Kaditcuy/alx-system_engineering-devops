#!/usr/bin/python3

"""
Script that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Fetches a subreddits number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        return json_data["data"]["subscribers"]
    else:
        return 0
