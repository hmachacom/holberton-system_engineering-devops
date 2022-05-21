#!/usr/bin/python3
"""Progress vs Score  Task Body Write a function that queries the
and prints the titles of the first 10 hot posts listed for a given
subreddit."""


def top_ten(subreddit):
    """subreddit
    Args:
        subreddit (str): subreddit
    """
    import requests

    url = requests.get(
        "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit),
        headers={"User-Agent": "platform"},
        allow_redirects=False,
    )
    if url.status_code == 200:
        for title in url.json().get("data").get("children"):
            print(title.get("data").get("title"))
    else:
        print("None")
