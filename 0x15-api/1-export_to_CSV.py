#!/usr/bin/python3
""" Gather data from an API and Export to CSV"""
import requests
import sys
import csv

if __name__ == "__main__":

    argv = sys.argv[1]
    name = (
        requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv)).json().get("username")
    )

    taskEmploy = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()
    with open('{}.csv'.format(argv), mode='w') as csvfile:
        writer = csv.writer(csvfile,  delimiter=',',
                            quoting=csv.QUOTE_ALL)
        for task in taskEmploy:
            if task.get('userId') == int(argv):
                tasksDone = task.get("completed")
                title = task.get("title")
                writer.writerow([argv, name, tasksDone, title])
