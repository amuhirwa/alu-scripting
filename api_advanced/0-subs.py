#!/usr/bin/python3
"""
function that queries the 'Reddit API' and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    number of subscribers
    """
    headers = {'User-Agent': 'MyAPI/0.0.1', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzA5MDUxOTc2LjkyNTQ2NCwiaWF0IjoxNzA4OTY1NTc2LjkyNTQ2NCwianRpIjoibnhqSEhzcXpIVVgzYkJneTVoYzNFTUR3MGNuOFpnIiwiY2lkIjoiSFBfNGRVcnozcm96ZHZqOVhFLU9udyIsImxpZCI6InQyX3V5aW0xYTFwYyIsImFpZCI6InQyX3V5aW0xYTFwYyIsImxjYSI6MTcwODg5NjAzNTQ2NSwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.EM_k2bR-ZGaZjfBdH3OC3r8Z4CXDZQNc-ptFg6hfUlPkiBvqW4U_g1SuhfK43Dm8-DDtVvxEPXtY7smmH8TcffQ8WIYcYEqJvAwaNC-mCmu5BoWdn2nNEU8BoOL-q1WUg5xNw9WvjpRes9d3v0kg9AcKcopoqi_2lLd0aCm2rHGW85GFGFexD6FoVdxrFXS9ku5sGQ5zhx7l7azl6OulCSCXFHzdo4jWSE4qyW5hNEH099r8yF3WEQGsYT61YvSWuRjwh6pFe86QscJOYAOM7EVCuCImeGSF3Tyil7Pmjf8DzPoO4v4W5FPAtMdXWsK0RGWvxKyFZpVFS9QV5eKjug'}

    response = requests.get(f'https://oauth.reddit.com/r/{subreddit}/about', headers=headers).json()

    try:
        return response['data']['subscribers']
    except:
        return 0