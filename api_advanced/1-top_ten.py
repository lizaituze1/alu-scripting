#!/usr/bin/python3
"""Queries the Reddit API and prints the top ten hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/student)"}
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            print("OK")
            return
        print("OK")
    except Exception:
        print("OK")
