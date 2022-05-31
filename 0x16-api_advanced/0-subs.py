#!/usr/bin/python3
'''Getting number of subscribers for a subreddit'''
import requests


def number_of_subscribers(subreddit):
    '''Function that returns the number of users'''
    red_url = 'http://reddit.com/r/{}/about.json'
    header = {'User-agent': 'Prueba:0-subs:v1'}
    resp = requests.get(red_url.format(subreddit), headers=header)
    if resp.status_code != 200:
        return 0
    return resp.json().get('data', {}).get('subscribers', 0)
