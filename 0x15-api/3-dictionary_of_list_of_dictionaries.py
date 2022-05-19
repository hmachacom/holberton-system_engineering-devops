#!/usr/bin/python3
""" Using what you did in the task #0, extend your
Python script to export data in the JSON format."""

if __name__ == "__main__":
    import requests
    import sys
    import json

    users = (requests.get("https://jsonplaceholder.typicode.com/users")).json()

    taskEmploy = (
        requests.get("https://jsonplaceholder.typicode.com/todos").json()
        )
    dictionary = {}

    for user in users:
        lista = []
        for task in taskEmploy:
            if task.get("userId") == user.get("id"):
                lista.append(
                    {
                        "username": user.get("username"),
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                    }
                )
        dictionary[user.get("id")] = lista

    with open("todo_all_employees.json", mode="w") as listFile:
        json.dump(dictionary, listFile)
