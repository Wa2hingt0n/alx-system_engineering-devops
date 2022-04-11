#!/usr/bin/python3
""" Exports information about an employees 'TODO list' progress in CSV
    format """
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(user_id)).json()
    employee_name = employee.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        for t in todos:
            writer.writerow(
                [user_id, employee_name, t.get("completed"), 
                 t.get("title")])
