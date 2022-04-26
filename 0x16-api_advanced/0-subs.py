#!/usr/bin/python3
""" Defines the function 'number_of_subscribers' that queries the reddit.com """
import requests


def number_of_subscribers(subreddit):
    """ Queries the reddit.com API and returns the number of subscribers for a
        given subreddit

    Args:
        subreddit (str): The subreddit whose number of subscribers is to be
                         returned.

    Returns:
        - The number of subscribers if the subreddit is valid
        - 0 if 'subreddit' is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        "User-Agent": "Your bot 0.1"
    }

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    subscribers = data.get("subscribers")
    return subscribers
