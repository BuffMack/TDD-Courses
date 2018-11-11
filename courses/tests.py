from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from courses.views import course_page
from courses.models import Course
from tkinter import *
import re

# Create your tests here.
class AddCoursePageTest(TestCase):
    def test_uses_course_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'course.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={
            'course_id': 1234,
            'course_name': 'A New Course', 
            'course_number': 'CIDM 3000',
            'semester': 'Fall 2017',
            'instructor': 'Dr Strange'
            })
        self.assertEqual(Course.objects.count(), 1)
        new_course = Course.objects.first()
        self.assertEqual(new_course.course_name, 'A New Course')      
    
    def test_redirects_after_POST(self):
        response = self.client.post('/', data={
            'course_id': 1234,
            'course_name': 'A New Course', 
            'course_number': 'CIDM 3000',
            'semester': 'Fall 2017',
            'instructor': 'Dr Strange'
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_displays_all_list_items(self):
        Course.objects.create(course_name='itemey 1')        
        Course.objects.create(course_name='itemey 2')        
        response = self.client.get('/')        
        self.assertIn('itemey 1', response.content.decode())        
        self.assertIn('itemey 2', response.content.decode())
        
class CourseModelTest(TestCase):
    def test_saving_and_retrieving_courses(self):
        first_course = Course()
        first_course.course_number = 'CIDM 1000'
        first_course.course_name = 'Intro to Computers'
        first_course.semester = 'Spring 2017'
        first_course.instructor = 'Dr Doom'
        first_course.save()

        second_course = Course()
        second_course.course_number = 'CIDM 6000'
        second_course.course_name = 'Advanced Programming'
        second_course.semester = 'Fall 2018'
        second_course.instructor = 'Dr MacTaggert'
        second_course.save()

        saved_courses = Course.objects.all()
        self.assertEqual(saved_courses.count(), 2)

        first_saved_course = saved_courses[0]
        second_saved_course = saved_courses[1]
        self.assertEqual(first_saved_course.course_name, 'Intro to Computers')
        self.assertEqual(second_saved_course.course_name, 'Advanced Programming')
    
    def test_removing_course(self):
        first_course = Course()
        first_course.course_number = 'CIDM 1000'
        first_course.course_name = 'Intro to Computers'
        first_course.semester = 'Spring 2017'
        first_course.instructor = 'Dr Doom'
        first_course.save()

        saved_courses = Course.objects.all()
        self.assertEqual(saved_courses.count(), 1)

        saved_courses_empty = Course.objects.exclude(course_number='CIDM 1000')
        self.assertEqual(saved_courses_empty.count(), 0)

class EditCoursePageTest(TestCase):
    def test_adding_checkbox_with_course_name_as_value(self):
        first_course = Course()
        first_course.course_number = 'CIDM 1000'
        first_course.course_name = 'Intro to Computers'
        first_course.semester = 'Spring 2017'
        first_course.instructor = 'Dr Doom'
        first_course.save()

        self.master = Tk()
        value1 = first_course.course_number
        first_course_cb = Checkbutton(self.master, text="course", variable=value1)
    
    def text_can_get_id_from_url(self):
        urlstring = '/courses/1234'
        id = re.findall('\d+', urlstring)
        self.assertEqual(id, 1234)
