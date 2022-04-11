#!/usr/bin/python3
""" Returns information about an employees 'TODO list' progress """
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    for done in todos:
        if done.get("completed") is True:
            completed = done.get("title")
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todos)))

    for line in completed:
        print("\t {}".format(line))
