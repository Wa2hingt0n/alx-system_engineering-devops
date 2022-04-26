#!/usr/bin/python3
""" Defines a function that prints top ten hot posts for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ Queries the reddit.com API and returns a list containing the titles
    of all hot articles for a given subreddit

    Args:
        subreddit (str): name of subreddit
        hot_list (list): list of titles
        after (str): id of next set of results
    """
    url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my bot 0.1'}
    response = requests.get(
        '{}{}/hot?after={}'.format(
            url,
            subreddit, after), headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None
    else:
        hot_articles = response.json()
        if len(hot_articles['data']['children']) == 0:
            return hot_list
        else:
            for d in hot_articles['data']['children']:
                hot_list.append(d['data']['title'])

            after = hot_articles['data']['after']
            if after is None:
                return hot_list
            return recurse(subreddit, hot_list, after=after)
