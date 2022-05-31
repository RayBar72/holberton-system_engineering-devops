#!/usr/bin/python3
'''Getting top 10 hot posts'''
import requests


def top_ten(subreddit):
    '''Function that returns the top ten hot posts titles'''
    red_url = 'http://reddit.com/r/{}/hot.json'
    header = {'User-agent': 'Prueba:1-top_ten:v1'}
    resp = requests.get(red_url.format(subreddit), headers=header)
    inf = resp.json().get('data', {}).get('children', {})
    if resp.status_code != 200:
        return print('None')
    for x in inf[0:10]:
        print(x.get('data', {}).get('title'))
