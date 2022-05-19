#!/usr/bin/python3
""" Gather data from an API """
from sys import argv
import requests

if __name__ == "__main__":
    name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    ).json().get('name')

    taskEmploy = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
        ).json()
    tasksDone = 0
    tasksTotal = 0
    nameTaskDone = []
    for task in taskEmploy:
        if task.get("completed"):
            tasksDone += 1
            nameTaskDone.append(task.get("title"))
        tasksTotal += 1
    print(f"Employee {name} is done with tasks({tasksDone}/{tasksTotal}):")
    print("\t ", end="")
    print("\n\t ".join(nameTaskDone))