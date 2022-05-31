#!/usr/bin/python3
'''
Recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''Getting all posto of hot'''
    red_url = 'http://reddit.com/r/{}/hot.json'
    header = {'User-agent': 'Prueba:1-top_ten:v1'}
    limit = {'limit': 100}
    if isinstance(after, str):
        if after != 'STOP':
            limit['after'] = after
        else:
            return hot_list
    resp = requests.get(red_url.format(subreddit), headers=header,
                        params=limit)
    if resp.status_code != 200:
        return None
    data = resp.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = 'STOP'
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
