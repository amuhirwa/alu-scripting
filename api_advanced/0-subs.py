"""Script that fetch 10 hot post for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for the given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    print(headers)
    response = requests.get(url, headers=headers, allow_redirects=False)
    print(response)
    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
    return 0
