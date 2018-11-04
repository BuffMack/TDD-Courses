from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from courses.views import course_page
from courses.models import Course

# Create your tests here.
class AddCoursePageTest(TestCase):
    def test_uses_course_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'course.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'course_name': 'A New Course'})
        self.assertIn('A New Course', response.content.decode())
        self.assertTemplateUsed(response, 'course.html')

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