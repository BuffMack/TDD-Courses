from selenium import webdriver
import unittest

class NewCourseEntryTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def teardDown(self):
        self.browser.quit()

    def test_form_displays_correctly(self):
        # After Professor Xavier logs into the system he navigates to the 'add courses' page.
        self.browser.get('http://localhost:8000')

        self.assertIn('Add Courses', self.browser.title)
        self.fail('Finish the test!')

        # He sees an input form that allows him to add data about the course. 
        # There are textboxes Course Name and Course Number
        # their are dropdown boxes to select the correct semester and professor.
# There is a text area that allows him to add a course description. 
# A save button at the bottom adds the data to the system; a cancel button clears the form.
# Once the course is added it displays in a list on the bottom.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
