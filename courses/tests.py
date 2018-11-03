from django.urls import resolve
from django.test import TestCase
from courses.views import course_page

# Create your tests here.
class AddCoursePageTest(TestCase):
    def test_root_url_resolves_to_course_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, course_page)
