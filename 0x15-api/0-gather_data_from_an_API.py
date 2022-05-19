#!/usr/bin/python3
""" Gather data from an API """
import json
from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    ) as nameEmploy:
        date = json.load(nameEmploy)
        name = date.get("name")
        id = date.get("id")
        with urllib.request.urlopen(
            f"https://jsonplaceholder.typicode.com/users/{id}/todos"
        ) as taskEmploy:
            tasksDone = 0
            tasksTotal = 0
            nameTaskDone = []
            for task in json.load(taskEmploy):
                if task.get("completed"):
                    tasksDone += 1
                    nameTaskDone.append(task.get("title"))
                tasksTotal += 1
        print(f"Employee {name} is done with tasks({tasksDone}/{tasksTotal}):")
        print("\t ", end="")
        print("\n\t ".join(nameTaskDone))
