#!/usr/bin/python3
""" Progress vs Score  Task Body Write a  recursive function  that queries the
and returns a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit, the function
should return None. """

import requests
import sys

all_hot = None


def recurse(subreddit, hot_list=[]):
    """_summary_

    Args:
        subreddit (_type_): _description_
        hot_list (list, optional): _description_. Defaults to [].

    Returns:
        _type_: _description_
    """
    global all_hot
    headers = {"User-Agent": "platform"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {"after": all_hot}
    response = requests.get(
        url, headers=headers, allow_redirects=False, params=parameters
    )

    if response.status_code == 200:
        next_ = response.json().get("data").get("all_hot")
        if next_ is not None:
            all_hot = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get("data").get("children")
        for title_ in list_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return None
