import os
from ast import literal_eval
from collections import Counter 


def find_groups(techniques,softwares):
	
	
	f = open("groupInfo.txt", "r")
	data = f.read()
	data = literal_eval(data)
	techniques = techniques.split(",")
	softwares = softwares.split(",")
	rate = {}

	for group in data:
		rate[group] = 0
		for technique in techniques:
			for group_technique in data[group]["techniques"]:
				if technique.lower() in group_technique.lower():
					rate[group] += 1
		for software in softwares:
			for group_technique in data[group]["techniques"]:
				if software.lower() in group_technique.lower():
					rate[group] += 1

	result = Counter(rate)
	result = result.most_common(5)
	return(result)
