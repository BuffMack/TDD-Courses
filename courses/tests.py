from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from courses.views import course_page

# Create your tests here.
class AddCoursePageTest(TestCase):
    def test_root_url_resolves_to_course_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, course_page)
    
    def test_course_page_returns_correct_html(self):
        request = HttpRequest()
        response = course_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Add A Course</title>', html)
        self.assertTrue(html.endswith('</html>'))
