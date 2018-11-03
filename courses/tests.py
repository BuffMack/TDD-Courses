from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from courses.views import course_page

# Create your tests here.
class AddCoursePageTest(TestCase):
    def test_uses_course_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'course.html')
