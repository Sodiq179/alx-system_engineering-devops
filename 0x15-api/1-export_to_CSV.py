#!/usr/bin/python3
"""Script to get info about user todo """

import json
import sys
import urllib.request

try:
	userId = int(sys.argv[1])
	file_name = "{}.csv".format(userId)
except:
	print("User id must be an integer")
	exit()

userInfo = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{id}'.format(id=userId))
userInfo = userInfo.read()
userName = json.loads(userInfo.decode("utf-8"))["username"]


request_url = urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos'.format(id=userId))
response_message = request_url.read()
response_message =  json.loads(response_message.decode("utf-8"))

userTotalTodos = []
for userDetails in response_message:
	if userDetails["userId"] == userId:
		userTotalTodos.append(userDetails)


def userTodoInfo():
	"""Exports information about a user todo into csv file"""
	with open(file_name, "w") as csvFile:
		for userInfo in userTotalTodos:
			entry = '"{}","{}","{}","{}"\n'.format(userId, userName, userInfo["completed"], userInfo["title"])
			csvFile.writelines(entry) 


if __name__ == "__main__":
	userTodoInfo()
