from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course_page(request):
    return HttpResponse('<html><title>Add A Course</title></html>')
