#!/usr/bin/python3
"""Reads todo list from apy for employee id"""
from sys import argv
import requests


if __name__ == '__main__':
    id = argv[1]
    us_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    tod_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)

    resp_todo = requests.get(tod_url).json()
    resp_user = requests.get(us_url).json()
    # print(resp_todo)
    # print(resp_user)

    total = 0
    completed = 0
    completed_task = []

    for task in resp_todo:
        total += 1
        if task.get('completed') is True:
            completed += 1
            completed_task.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(resp_user.get('name'), completed, total))
    for c in completed_task:
        print("\t{}".format(c))
