#!/usr/bin/python3
""" Gather data from an API """
import requests
import sys

if __name__ == "__main__":

    argv = sys.argv[1]
    name = (
        requests.get(f"https://jsonplaceholder.typicode.com/users/{argv}")
        .json()
        .get("name")
    )

    taskEmploy = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()
    tasksDone = 0
    tasksTotal = 0
    nameTaskDone = []
    for task in taskEmploy:
        if task.get("completed") and task.get('userId') == int(argv):
            tasksDone += 1
            nameTaskDone.append(task.get("title"))
        tasksTotal += 1
    print(f"Employee {name} is done with tasks({tasksDone}/{tasksTotal}):")
    print("\t ", end="")
    print("\n\t ".join(nameTaskDone))
