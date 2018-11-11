from django.shortcuts import render
from django.http import HttpResponse
import json
from apirequests import views

def groupStudents(request):
	#define group size
	size = 3	
	#HttpResponse from apirequests app's studentsFromCourse function
	#Currently parameter doesn't affect return value.
	resp = views.studentsFromCourse(1)
	#using Python's json library to extract the content
	data = json.loads(resp.content)
	#some assisting variables
	groups = []
	group = []
	j = 0
	groupsastext = ''
	#group logic
	for i in range(data['count']):
		studentObject = data['results'][i]
		if j < size:
			group.append(studentObject)
			j += 1
		else:
			groups.append(group)
			group = [studentObject]
			j = 1
	if (len(group) != 0):
		groups.append(group)
	
	#builds a string representation of the data	
	for i in range(len(groups)):
		if i == 0:
			groupsastext += ('group '+ str(i+1) +':')
		else:
			groupsastext += ('\ngroup '+ str(i+1) +':')
		for j in groups[i]:
			groupsastext += '\n' +str(j)
			
	return HttpResponse(groupsastext, content_type='text/plain')
