#!/usr/bin/python3
"""Script to get info about user todo """
import json
import sys
import urllib.request

def getUserDetails(userId):
	"""Use user id to get necessary informations"""
	userInfo = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{id}'.format(id=userId))
	userInfo = userInfo.read()
	userName = json.loads(userInfo.decode("utf-8"))["username"]


	request_url = urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos')
	response_message = request_url.read()
	response_message =  json.loads(response_message.decode("utf-8"))

	userTotalTodos = []
	for userDetails in response_message:
		if userDetails["userId"] == userId:
			userTotalTodos.append(userDetails)

	return userName, userTotalTodos


def userTodoInfo():
	"""Exports information about a user todo into json file"""
	jsonContent = {}
	for userId in range(1, 11):
		userName, userTotalTodos = getUserDetails(userId)	
		jsonContent[userId] = []
		for userInfo in userTotalTodos:
			entry = {"task": userInfo["title"], "completed": userInfo["completed"], "username": userName}
			jsonContent[userId].append(entry) 

	# Serializing json
	json_object = json.dumps(jsonContent)

	# Writing to sample.json
	with open("todo_all_employees.json", "w") as outfile:
		outfile.write(json_object)


if __name__ == "__main__":
	userTodoInfo()
