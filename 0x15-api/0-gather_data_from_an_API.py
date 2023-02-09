#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the body of the response according to id of employee
"""
import requests
import sys


def todo_list_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_data = requests.get(url).json()
    employee_name = employee_data['name']

    url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(employee_id)
    todos = requests.get(url).json()

    done_tasks = [task['title'] for task in todos if task['completed']]
    done_tasks_count = len(done_tasks)
    total_tasks_count = len(todos)

    result = "Employee {} is done with tasks({}/{}):\n".format(
        employee_name, done_tasks_count, total_tasks_count)
    for task in done_tasks:
        result += "\t {}\n".format(task)

    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_list_progress.py [employee_id]")
    else:
        employee_id = int(sys.argv[1])
        print(todo_list_progress(employee_id), end='')
