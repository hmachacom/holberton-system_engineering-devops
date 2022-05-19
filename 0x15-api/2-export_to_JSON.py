#!/usr/bin/python3
""" Using what you did in the task #0, extend your
Python script to export data in the JSON format."""

if __name__ == "__main__":
    import requests
    import sys
    import json
    argv = sys.argv[1]
    users = (
        requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv))
    ).json()

    taskEmploy = (
        requests.get("https://jsonplaceholder.typicode.com/todos")
        .json()
        )
    with open('{}.json'.format(argv), mode="w") as listFile:
        lista = []
        for task in taskEmploy:
            lista.append(
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": users.get("username"),
                }
            )
        dictionary = {"{}".format(argv): lista}
        json.dump(dictionary, listFile)
