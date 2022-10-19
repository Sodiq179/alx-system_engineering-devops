#!/usr/bin/python3
"""Script to get info about user todo """

import json
import sys
import urllib.request

try:
	userId = int(sys.argv[1])

except:
	print("User id must be an integer")
	exit()

userInfo = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{id}'.format(id=userId))
userInfo = userInfo.read()
employeeName = json.loads(userInfo.decode("utf-8"))["name"]


request_url = urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos'.format(id=userId))
response_message = request_url.read()
response_message =  json.loads(response_message.decode("utf-8"))

userTotalTodos = []
doneTasks = []

for userDetails in response_message:

	if userDetails["userId"] == userId:
		userTotalTodos.append(userDetails)

	if userDetails["userId"] == userId and userDetails["completed"] == True:
                doneTasks.append(userDetails)


def userTodoInfo():
	"""Gives information about a user todo"""
	print("Employee {} is done with tasks({}/{}):".format(employeeName,len(doneTasks),len(userTotalTodos)))
	for userInfo in doneTasks:
		print("\t {}\n".format(userInfo["title"]))


if __name__ == "__main__":
	userTodoInfo()
