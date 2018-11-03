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

        # The page title and header asks him to add a course
        self.assertIn('Add A Course', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Add a new course to the system', header_text)

        # He sees an input form that allows him to add data about the course. 
        form = self.browser.find_element_by_id('form_course')
        self.assertEqual(
            form.get_attribute('method'),
            'post'
        )

        # There are textboxes Course Name and Course Number
        course_name = self.browser.find_element_by_id('course_name')
        self.assertEqual(course_name.get_attribute('type'),'text')
        self.assertEqual(course_name.get_attribute('placeholder'),'Enter a Course Name')

        course_number = self.browser.find_element_by_id('course_number')
        self.assertEqual(course_number.get_attribute('type'),'text')
        self.assertEqual(course_number.get_attribute('placeholder'),'Enter a Course Number')

        # There is a dropdown box to select the semester during which the course took place.
        semester = self.browser.find_element_by_id('semester')
        semesters = semester.find_elements_by_tag_name('option')
        self.assertGreater(len(semesters), 1)
        self.assertEqual(semesters[0].text, 'Select a Semester')
        # the dropdown for semester allows Prof X to enter courses that took place between the current semester and two years back (10 total semesters)
        self.assertEqual(semesters[1].text, 'Fall 2016') #test to see if the first option (not counting the default select option) is set to the first eligible semester
        self.assertEqual(len(semesters), 11) #test for ten semesters plus the default select option in the list

        # There is a dropdown box to select the course instructor.
        instructor = self.browser.find_element_by_id('instructor')
        instructors = instructor.find_elements_by_tag_name('option')
        self.assertGreater(len(instructors), 1)
        self.assertEqual(instructors[0].text, 'Select an Instructor')
        # the dropdown for instructor allows Prof X to select any of the five instructors who teach in the department, including department chair Dr Moira MacTaggert
        self.assertEqual(instructors[1].text, 'Dr MacTaggert') #test to see if the first option (not counting the default select option) is set to the department chair
        self.assertEqual(len(instructors), 6) #test for five instructors plus the default select option in the list

        # There is a text area that allows him to add a course description. 
        description = self.browser.find_element_by_id('description')
        self.assertEqual(description.get_attribute('type'),'textarea')
        self.assertEqual(description.get_attribute('placeholder'),'Enter a Description')

        # A save button at the bottom adds the data to the system; a cancel button clears the form.
        # Once the course is added it displays in a list on the bottom.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
