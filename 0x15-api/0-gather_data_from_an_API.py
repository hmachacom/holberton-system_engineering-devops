#!/usr/bin/python3
""" Gather data from an API """
import urllib.request
import json
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users"
    ) as nameEmploy:

        for i in json.load(nameEmploy):
            if i["id"] == int(argv[1]):
                name = i["name"]
                id = i["id"]
        with urllib.request.urlopen(
            f"https://jsonplaceholder.typicode.com/users/{id}/todos"
        ) as taskEmploy:
            tasksDone = 0
            tasksTotal = 0
            nameTaskDone = []
            for task in json.load(taskEmploy):
                if task["completed"]:
                    tasksDone += 1
                    nameTaskDone.append(task["title"])
                tasksTotal += 1
        print(f"Employee {name} is done with tasks({tasksDone}/{tasksTotal}):")
        print("\t ", end='')
        print('\n\t '.join(nameTaskDone))
