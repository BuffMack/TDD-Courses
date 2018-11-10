from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
import unittest
import time
from courses.models import Course


MAX_WAIT = 10

class NewCourseEntryTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def teardDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('course_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def check_for_new_course_in_list(self, row_text):
        start_time = time.time()

        while True:
            try:
                table = self.browser.find_element_by_id('course_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])

                return
            
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e

                time.sleep(0.5)
    
    def test_layout_styling(self):
        self.browser.get(self.live_server_url)
        #check to see if bootstrap is installed and rendering
        card = self.browser.find_elements_by_class_name('card')
        self.assertNotEqual(card.count, 0)

    # def test_form_displays_correctly(self):
    #     # After Professor Xavier logs into the system he navigates to the 'add courses' page.
    #     #self.browser.get('http://localhost:8000') 
    #     self.browser.get(self.live_server_url)

    #     # The page title and header asks him to add a course
    #     self.assertIn('Add A Course', self.browser.title)
    #     header_text = self.browser.find_element_by_tag_name('h1').text
    #     self.assertIn('Add a new course to the system', header_text)

    #     # He sees an input form that allows him to add data about the course. 
    #     form = self.browser.find_element_by_id('form_course')
    #     self.assertNotEqual(
    #         form.get_attribute('method'),
    #         'POST'
    #     )

    #     # # There are textboxes Course Name and Course Number
    #     course_name = self.browser.find_element_by_id('course_name')
    #     self.assertEqual(course_name.get_attribute('type'),'text')
    #     self.assertEqual(course_name.get_attribute('placeholder'),'Enter a Course Name')

    #     course_number = self.browser.find_element_by_id('course_number')
    #     self.assertEqual(course_number.get_attribute('type'),'text')
    #     self.assertEqual(course_number.get_attribute('placeholder'),'Enter a Course Number')

    #     # # There is a dropdown box to select the semester during which the course took place.
    #     semester = self.browser.find_element_by_id('semester')
    #     semesters = semester.find_elements_by_tag_name('option')
    #     self.assertGreater(len(semesters), 1)
    #     self.assertEqual(semesters[0].text, 'Select a Semester')
    #     # # the dropdown for semester allows Prof X to enter courses that took place between the current semester and two years back (10 total semesters)
    #     self.assertEqual(semesters[1].text, 'Fall 2016') #test to see if the first option (not counting the default select option) is set to the first eligible semester
    #     self.assertEqual(len(semesters), 11) #test for ten semesters plus the default select option in the list

    #     # # There is a dropdown box to select the course instructor.
    #     instructor = self.browser.find_element_by_id('instructor')
    #     instructors = instructor.find_elements_by_tag_name('option')
    #     self.assertGreater(len(instructors), 1)
    #     self.assertEqual(instructors[0].text, 'Select an Instructor')
    #     # # the dropdown for instructor allows Prof X to select any of the five instructors who teach in the department, including department chair Dr Moira MacTaggert
    #     self.assertEqual(instructors[1].text, 'Dr MacTaggert') #test to see if the first option (not counting the default select option) is set to the department chair
    #     self.assertEqual(len(instructors), 6) #test for five instructors plus the default select option in the list

    #     # # There is a text area that allows him to add a course description. 
    #     # description = self.browser.find_element_by_id('description')
    #     # self.assertEqual(description.get_attribute('type'),'textarea')
    #     # self.assertEqual(description.get_attribute('placeholder'),'Enter a Description')

    #     # A save button at the bottom adds the data to the system; a cancel button clears the form.

    # def test_form_saves_course_on_submit(self):
    #     # Professor X adds a new class 'Intro to Computers'
    #     self.browser.get(self.live_server_url)
    #     course_number = self.browser.find_element_by_id('course_number')
    #     course_number.send_keys('CIDM 1000')

    #     course_name = self.browser.find_element_by_id('course_name')
    #     course_name.send_keys('Intro to Computers')
        
    #     course_name.send_keys(Keys.ENTER)
    #     time.sleep(1)
    #     self.check_for_row_in_list_table('Intro to Computers')

    #     # course_name.send_keys('Advance Computing')
    #     # course_name.send_keys(Keys.ENTER)
    #     # time.sleep(1)
    #     #self.check_for_new_course_in_list('Advance Computing')
    #     self.fail('Finish the test!')
    
    def test_can_edit_existing_course(self):
        self.browser.get(self.live_server_url)
        # Professor X adds a new course to the system
        course_number = self.browser.find_element_by_id('course_number')
        course_number.send_keys('CIDM 1000')
        course_name = self.browser.find_element_by_id('course_name')
        course_name.send_keys('Intro to Computerses')       
        semester = self.browser.find_element_by_id('semester')
        semesterOptions = semester.find_elements_by_tag_name('option')
        semesterOptions[4].click() 
        instructor = self.browser.find_element_by_id('instructor')
        instructorOptions = instructor.find_elements_by_tag_name('option')
        instructorOptions[2].click() 

        course_name.send_keys(Keys.ENTER)
        time.sleep(1)

        # He notices that he misspelled the name, so he clicks the checkbox next to the course name
        # and hits the edit button to fix his mistake
        course_number_edit = self.browser.find_element_by_id("cb_course_number").get_attribute("value")
        btn_course_edit = self.browser.find_element_by_name('btn_course_edit')

        # The form is repopulated with the values for the course that he wants to edit.
        courses = Course.objects.all()
        courseToEdit = courses.filter(course_number__startswith=course_number_edit).values()
        print(courseToEdit)
        print(courseToEdit[0]['course_name'])

        course_name_2 = self.browser.find_element_by_id('course_name')
        course_name_2.send_keys(courseToEdit[0]['course_name'])
        course_number_2 = self.browser.find_element_by_id('course_number')
        course_number_2.send_keys(courseToEdit[0]['course_number'])

        semester2 = self.browser.find_element_by_id('semester')
        semesterOptions2 = semester2.find_elements_by_tag_name('option')
        semesterIndex2 = self.find_option_selectedIndex(semesterOptions2, courseToEdit[0]['semester'])
        semesterOptions2[semesterIndex2].click() 

        instructor2 = self.browser.find_element_by_id('instructor')
        instructorOptions2 = instructor2.find_elements_by_tag_name('option')
        instructorIndex2 = self.find_option_selectedIndex(instructorOptions2, courseToEdit[0]['instructor'])
        instructorOptions2[instructorIndex2].click() 
        
        # On clicking 'Add Course' again is also removed from the list until the editing is done
        course_name_3 = self.browser.find_element_by_id('course_name')
        course_name_3.clear()
        course_name_3.send_keys('Intro to Computers')
        course_name_3.send_keys(Keys.ENTER)
        time.sleep(1)

        self.fail('Finish the test!')
    
    def find_option_selectedIndex(self,options,value):
        counter = 0
        for option in options:
            if option.get_attribute('value') == value:
                return counter;
                #break;
            else:
                counter = counter + 1
    


