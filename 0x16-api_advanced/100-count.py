#!/usr/bin/python3
"""
queries the Reddit API and returns the titles of a given subreddit.
If an invalid subreddit is given, the function should return None. and
prints a sorted count of given keywords (case-insensitive, delimited by spaces
"""

import requests


def count_words(subreddit, word_list, counts=None, after=None):
    if counts is None:
        counts = {}

    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                     after)

    headers = {
        "User-Agent": "anything"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")

    for child in children:
        title = child.get("data").get("title")
        words = title.lower().split()
        for word in word_list:
            if word.lower() in words:
                if word.lower() in counts:
                    counts[word.lower()] += words.count(word.lower())
                else:
                    counts[word.lower()] = words.count(word.lower())

    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for count in sorted_counts:
            print("{}: {}".format(count[0], count[1]))
    else:
        return count_words(subreddit, word_list, counts, after)
