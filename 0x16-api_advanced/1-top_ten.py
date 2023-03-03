#!/usr/bin/python3

"""
Script that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Prints a subreddits 10 of hotposts"""

    listing = "hot"
    url = "https://www.reddit.com/r/{}/{}.json".format(subreddit, listing)
    headers = {"User-agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        hot_posts = []
        for i, post in enumerate(json_data['data']['children']):
            if i >= 10:
                break
            titles = post['data']['title']
            hot_posts.append(titles)
        for items in hot_posts:
            print(items)
    else:
        print('None')
