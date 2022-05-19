#!/usr/bin/python3
""" Gather data from an API and Export to CSV"""
import requests
import sys
import csv

if __name__ == "__main__":

    argv = sys.argv[1]
    name = (
        requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv))
        .json()
        .get("username")
    )

    taskEmploy = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()
    with open('{}.csv'.format(argv), 'w') as csvfile:
        writer = csv.writer(csvfile,  delimiter=',',
                            quoting=csv.QUOTE_ALL)
        for task in taskEmploy:
            if task.get('userId') == int(argv):
                id = task.get('userId')
                tasksDone = str(task.get("completed"))
                title = str(task.get("title"))
                writer.writerow([id, name, tasksDone, title])
