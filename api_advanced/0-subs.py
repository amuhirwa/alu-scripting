#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for the given subreddit."""
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']
        if data:
            return data['subscribers']
    return 0
