#!/usr/bin/python3
"""
function that queries the 'Reddit API' and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    number of subscribers
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}

    response = requests.get(f'https://oauth.reddit.com/r/{subreddit}/about', headers=headers).json()

    return response['data']['subscribers']