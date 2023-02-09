#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in JSON format.
File name must be: todo_all_employees.json
"""
from json import dumps
import requests


def todo_list_progress(response, employee):
    """Get all the tasks of an employee
    """
    result = list()

    for task in response:
        if task.get('userId') == employee.get('id'):
            task_data = {
                'username': employee.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed'),
            }

            result.append(task_data)

    return result


if __name__ == '__main__':
    # Main formatted names to API uris and filenames
    main_url = 'https://jsonplaceholder.typicode.com'
    users_uri = '{api}/users'.format(api=main_url)
    todos_uri = '{api}/todos'.format(api=main_url)
    filename = 'todo_all_employees.json'

    # Users Response
    users = requests.get(users_uri).json()

    # Users TODO Response
    tasks = requests.get(todos_uri).json()

    users_tasks = dict()

    # Stores all the tasks of each employee in the API data
    for user in users:
        user_id = user.get('id')

        # A list of all tasks of current employee
        user_tasks = todo_list_progress(tasks, {
            'id': user_id,
            'username': user.get('username')
        })

        # Inserting the list of all tasks of current employee
        # to a dictionary that stores all the employees with their tasks.
        users_tasks[user_id] = user_tasks

    # Create the new file with all the information
    # Filename example: `todo_all_employees.json`
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps(users_tasks))
