from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import Course
import random
import re

# Create your views here.
def course_page(request):
    if request.method == 'POST':
        urlstring = request.build_absolute_uri()
        # I'm not positive how to do a correct ternary statement here in python so I'm taking the long route
        course_id_test = 0 
        if request.POST['course_id']:
            course_id_test = request.POST['course_id']
        print(course_id_test)
        if Course.objects.filter(course_id=course_id_test).exists():
            Course.objects.filter(course_id=course_id_test).update(
            course_number=request.POST['course_number'],
            course_name=request.POST['course_name'],
            semester=request.POST['semester'],
            instructor=request.POST['instructor'])
        else:
            Course.objects.create(
                course_id = random.randint(10000,99999),
                course_number=request.POST['course_number'],
                course_name=request.POST['course_name'],
                semester=request.POST['semester'],
                instructor=request.POST['instructor'])
        return redirect('/')
    
    course = Course()
    courses = Course.objects.all()
    course_id_edit = 0

    if request.method == 'GET':
        if request.GET.get('id') is not None:
            course_id_edit = request.GET.get('id')

        course = Course.objects.filter(course_id=course_id_edit).first()

    return render(request, 'course.html', {'courses': courses, 'course': course})


