from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import Course

# Create your views here.
def course_page(request):
    if request.method == 'POST':
        Course.objects.create(
            course_number=request.POST['course_number'],
            course_name=request.POST['course_name'],
            semester=request.POST['semester'],
            instructor=request.POST['instructor'])
        # print('Course Name: ')
        # print(request.POST['course_name'])
        return redirect('/')

    courses = Course.objects.all()
    # print(courses)
    return render(request, 'course.html', {'courses': courses})


    #      return HttpResponse(request.POST['course_name'])
    # return render(request, 'course.html')
    # return render(request, 'course.html', {        
    #     'new_course_name': courses[0].course_name,
    # })

