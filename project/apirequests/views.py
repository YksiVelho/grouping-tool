from django.shortcuts import render
from django.http import HttpResponse
from project.credentials import API_TOKEN
import requests

#Returns all users from api
def getUsers():
    users = requests.get('http://localhost:8000/api/v2/users/',
                            headers={'Authorization': f'Token {API_TOKEN}'})
    return HttpResponse(users)

#Returns all courses from api
def getCourses():
    courses = requests.get('http://localhost:8000/api/v2/courses/',
                            headers={'Authorization': f'Token {API_TOKEN}'})
    return HttpResponse(courses)

#Returns user via their a-plus user ID
def findUser(user_id):
    user = requests.get(f'http://localhost:8000/api/v2/users/{user_id}',
                        headers={'Authorization': f'Token {API_TOKEN}'})
    if user.status_code == 200:
        return HttpResponse(user)
    else:
        return HttpResponse(f'Something went wrong finding user. Is the user_id: {user_id} correct?')

#Returns all the students from course course id hard coded for testing purposes
def studentsFromCourse(courseID):
    courseID = 1
    students = requests.get(f'http://localhost:8000/api/v2/courses/{courseID}/students/',
                            headers={'Authorization': f'Token {API_TOKEN}'})
    if students.status_code == 200:
        return HttpResponse(students)
    else:
        return HttpResponse(f'Something went with your request. Is the courseID: {courseID} correct?')