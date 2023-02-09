#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in JSON format.
File name must be: USER_ID.json
"""
import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    username = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(emp_id)).json().get("username")
    all_tasks = []
    r = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(emp_id)):
            temp = {}
            temp["task"] = task.get("title")
            temp["completed"] = task.get("completed")
            temp["username"] = username
            all_tasks.append(temp)

    with open("{}.json".format(emp_id), 'w+') as jsonfile:
        json.dump({emp_id: all_tasks}, jsonfile)
