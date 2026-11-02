#!/usr/bin/python3
"""Recursively counts keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in all hot post titles."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    wanted = [word.lower() for word in word_list]

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except Exception:
        return

    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in wanted:
                counts[token] = counts.get(token, 0) + 1

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    totals = {}
    for word, number in counts.items():
        totals[word] = number * wanted.count(word)
    for word, number in sorted(totals.items(), key=lambda item:
                               (-item[1], item[0])):
        print("{}: {}".format(word, number))
