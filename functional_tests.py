from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        
    def test_can_access_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('CV', self.browser.title)

    def test_edit_submit_buttons(self):
        self.browser.get('http://localhost:8000')
        time.sleep(1)
        
#        Getting the uneditaable contents of the page and testing that
#       they display the correct value and that they are displaying
#       Also checking that the editable contents are not displaying
        edit_about_button=self.browser.find_element_by_id("edit_about")
        submit_about_button = self.browser.find_element_by_id("submit_about")
        editable_about_div = self.browser.find_element_by_id("editable_about")
        uneditable_about_div = self.browser.find_element_by_id("uneditable_about")
        
        uneditable_name_surname = self.browser.find_element_by_id("uneditable_name_surname")
        uneditable_address = self.browser.find_element_by_id("uneditable_address")
        uneditable_email = self.browser.find_element_by_id("uneditable_email")
        uneditable_about_description = self.browser.find_element_by_id("uneditable_about_description")
        
        self.assertEqual(uneditable_name_surname.text, "NAME SURNAME")
        self.assertEqual(uneditable_address.text, "ADDRESS")
        self.assertEqual(uneditable_email.text, "email@email.com")
        self.assertEqual(uneditable_about_description.text, "Short Description")
        
        self.assertEqual(editable_about_div.value_of_css_property('display'), "none")
        self.assertEqual(uneditable_about_div.value_of_css_property('display'), "block")
        
        edit_about_button.click();
        time.sleep(1)
        
#        Checking that the editable content has the right inputs
        editable_name_surname = self.browser.find_element_by_id("name_surname")
        editable_address = self.browser.find_element_by_id("address")
        editable_email = self.browser.find_element_by_id("email")
        editable_about_description = self.browser.find_element_by_id("about_description")
        
        self.assertEqual(editable_name_surname.text, "NAME SURNAME")
        self.assertEqual(editable_address.text, "ADDRESS")
        self.assertEqual(editable_email.text, "email@email.com")
        self.assertEqual(editable_about_description.text, "Short Description")
        
#        Changing the contents of the editable inputs
        editable_name_surname.click()
        editable_name_surname.clear()
        editable_name_surname.send_keys("JANE DOE")
        editable_address.click()
        editable_address.clear()
        editable_address.send_keys("UNKNOWN")
        editable_email.click()
        editable_email.clear()
        editable_email.send_keys("janedoe@email.com")
        editable_about_description.click()
        editable_about_description.clear()
        editable_about_description.send_keys("N/A")
        
        editable_about_div = self.browser.find_element_by_id("editable_about")
        uneditable_about_div = self.browser.find_element_by_id("uneditable_about")
        
        self.assertEqual(editable_about_div.value_of_css_property('display'), "block")
        self.assertEqual(uneditable_about_div.value_of_css_property('display'), "none")
        
        submit_about_button.click();
        time.sleep(1)
        
        edit_about_button=self.browser.find_element_by_id("edit_about")
        submit_about_button = self.browser.find_element_by_id("submit_about")
        editable_about_div = self.browser.find_element_by_id("editable_about")
        uneditable_about_div = self.browser.find_element_by_id("uneditable_about")
        
        uneditable_name_surname = self.browser.find_element_by_id("uneditable_name_surname")
        uneditable_address = self.browser.find_element_by_id("uneditable_address")
        uneditable_email = self.browser.find_element_by_id("uneditable_email")
        uneditable_about_description = self.browser.find_element_by_id("uneditable_about_description")
        
        self.assertEqual(uneditable_name_surname.text, "JANE DOE")
        self.assertEqual(uneditable_address.text, "UNKNOWN")
        self.assertEqual(uneditable_email.text, "janedoe@email.com")
        self.assertEqual(uneditable_about_description.text, "N/A")
        
        editable_about_div = self.browser.find_element_by_id("editable_about")
        uneditable_about_div = self.browser.find_element_by_id("uneditable_about")
        
        self.assertEqual(editable_about_div.value_of_css_property('display'), "none")
        self.assertEqual(uneditable_about_div.value_of_css_property('display'), "block")
        

class ExperiencePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_and_edit_new_entry(self) :
    
        self.browser.get('http://localhost:8000')
        time.sleep(1)
    
        add_button=self.browser.find_element_by_id("add_experience")
        add_button.click()
        time.sleep(1)
        
        title=self.browser.find_element_by_id("editable_job_title")
        company=self.browser.find_element_by_id("editable_job_company")
        description=self.browser.find_element_by_id("editable_job_description")
        dates=self.browser.find_element_by_id("editable_job_dates")
        submit_button = self.browser.find_element_by_id("submit_new_job")
        
        self.assertEqual(title.text, "ADD JOB TITLE")
        self.assertEqual(company.text, "ADD COMPANY")
        self.assertEqual(description.text, "Add short description")
        self.assertEqual(dates.text, "Add dates")
        
        title.click()
        title.clear()
        title.send_keys("DEVELOPER")
        
        company.click()
        company.clear()
        company.send_keys("APPLE")
        
        description.click()
        description.clear()
        description.send_keys("N/A")
        
        dates.click()
        dates.clear()
        dates.send_keys("SEPTEMBER 2020 - PRESENT")
        
        submit_button.click()
        
        time.sleep(1)
        
        added_title = self.browser.find_element_by_id('uneditable_job_title_1')
        added_company = self.browser.find_element_by_id('uneditable_job_company_1')
        added_description = self.browser.find_element_by_id('uneditable_job_description_1')
        added_dates = self.browser.find_element_by_id('uneditable_job_dates_1')
        
        self.assertEqual(added_title.text, "DEVELOPER")
        self.assertEqual(added_company.text, "APPLE")
        self.assertEqual(added_description.text, "N/A")
        self.assertEqual(added_dates.text, "SEPTEMBER 2020 - PRESENT")
        
        edit_button = self.browser.find_element_by_id('edit_experience_1')
        
        edit_button.click()
        
        editable_title = self.browser.find_element_by_id('editable_job_title_1')
        editable_company = self.browser.find_element_by_id('editable_job_company_1')
        editable_description = self.browser.find_element_by_id('editable_job_description_1')
        editable_dates = self.browser.find_element_by_id('editable_job_dates_1')
        submit_button = self.browser.find_element_by_id('submit_experience_1')

        self.assertEqual(editable_title.text, "DEVELOPER")
        self.assertEqual(editable_company.text, "APPLE")
        self.assertEqual(editable_description.text, "N/A")
        self.assertEqual(editable_dates.text, "SEPTEMBER 2020 - PRESENT")
        
        editable_title.click()
        editable_title.clear()
        editable_title.send_keys("DEVELOPER")
        
        editable_company.click()
        editable_company.clear()
        editable_company.send_keys("GOOGLE")
        
        editable_description.click()
        editable_description.clear()
        editable_description.send_keys("N/A")
        
        editable_dates.click()
        editable_dates.clear()
        editable_dates.send_keys("PRESENT - FUTURE")
        
        submit_button.click()
        time.sleep(1)
        
        title = self.browser.find_element_by_id('uneditable_job_title_1')
        company = self.browser.find_element_by_id('uneditable_job_company_1')
        description = self.browser.find_element_by_id('uneditable_job_description_1')
        dates = self.browser.find_element_by_id('uneditable_job_dates_1')

        self.assertEqual(title.text, "DEVELOPER")
        self.assertEqual(company.text, "GOOGLE")
        self.assertEqual(description.text, "N/A")
        self.assertEqual(dates.text, "PRESENT - FUTURE")
        
        
class EducationPageTest(unittest.TestCase):

    def setUp(self):
       self.browser = webdriver.Firefox()

    def tearDown(self):
       self.browser.quit()

    def test_can_add_and_edit_new_entry(self) :
    
        self.browser.get('http://localhost:8000')
        time.sleep(1)
        
        add_button = self.browser.find_element_by_id('add_education')
        add_button.click()
        time.sleep(1)
        
        add_school = self.browser.find_element_by_id('editable_school')
        add_qualification = self.browser.find_element_by_id('editable_qualification')
        add_description = self.browser.find_element_by_id('editable_education_description')
        add_grade = self.browser.find_element_by_id('editable_education_grade')
        add_dates = self.browser.find_element_by_id('editable_education_dates')
        submit = self.browser.find_element_by_id('submit_new_education')
        
        self.assertEqual(add_school.text, "ADD SCHOOL")
        self.assertEqual(add_qualification.text, "ADD QUALIFICATION")
        self.assertEqual(add_description.text, "Add description")
        self.assertEqual(add_grade.text, "Add grade")
        self.assertEqual(add_dates.text, "Add dates")
        
        add_school.click()
        add_school.clear()
        add_school.send_keys("UOB")

        add_qualification.click()
        add_qualification.clear()
        add_qualification.send_keys("CS")

        add_description.click()
        add_description.clear()
        add_description.send_keys("CS")

        add_grade.click()
        add_grade.clear()
        add_grade.send_keys("1ST")
        
        add_dates.click()
        add_dates.clear()
        add_dates.send_keys("SEPTEMBER 2019 - PRESENT")

        submit.click()
        time.sleep(1)
        
        school = self.browser.find_element_by_id('uneditable_school_1')
        qualification = self.browser.find_element_by_id('uneditable_qualification_1')
        description = self.browser.find_element_by_id('uneditable_education_description_1')
        grade = self.browser.find_element_by_id('uneditable_education_grade_1')
        dates = self.browser.find_element_by_id('uneditable_education_dates_1')
        edit = self.browser.find_element_by_id('edit_education_1')
        
        self.assertEqual(school.text, "UOB")
        self.assertEqual(qualification.text, "CS")
        self.assertEqual(description.text, "CS")
        self.assertEqual(grade.text, "1ST")
        self.assertEqual(dates.text, "SEPTEMBER 2019 - PRESENT")
        
        edit.click()
        time.sleep(1)
        
        edit_school = self.browser.find_element_by_id('editable_school_1')
        edit_qualification = self.browser.find_element_by_id('editable_qualification_1')
        edit_description = self.browser.find_element_by_id('editable_education_description_1')
        edit_grade = self.browser.find_element_by_id('editable_education_grade_1')
        edit_dates = self.browser.find_element_by_id('editable_education_dates_1')
        submit = self.browser.find_element_by_id('submit_education_1')
        
        self.assertEqual(edit_school.text, "UOB")
        self.assertEqual(edit_qualification.text, "CS")
        self.assertEqual(edit_description.text, "CS")
        self.assertEqual(edit_grade.text, "1ST")
        self.assertEqual(edit_dates.text, "SEPTEMBER 2019 - PRESENT")
        
        edit_school.click()
        edit_school.clear()
        edit_school.send_keys("CNGRC")

        edit_qualification.click()
        edit_qualification.clear()
        edit_qualification.send_keys("MI")

        edit_description.click()
        edit_description.clear()
        edit_description.send_keys("MI")

        edit_grade.click()
        edit_grade.clear()
        edit_grade.send_keys("9.65")
        
        edit_dates.click()
        edit_dates.clear()
        edit_dates.send_keys("SEPTEMBER 2014 - JUNE 2018")
        
        submit.click()
        time.sleep(1)

        school = self.browser.find_element_by_id('uneditable_school_1')
        qualification = self.browser.find_element_by_id('uneditable_qualification_1')
        description = self.browser.find_element_by_id('uneditable_education_description_1')
        grade = self.browser.find_element_by_id('uneditable_education_grade_1')
        dates = self.browser.find_element_by_id('uneditable_education_dates_1')
        edit = self.browser.find_element_by_id('edit_education_1')
        
        self.assertEqual(school.text, "CNGRC")
        self.assertEqual(qualification.text, "MI")
        self.assertEqual(description.text, "MI")
        self.assertEqual(grade.text, "9.65")
        self.assertEqual(dates.text, "SEPTEMBER 2014 - JUNE 2018")
        
class InterestsPageTest(unittest.TestCase):

    def setUp(self):
       self.browser = webdriver.Firefox()

    def tearDown(self):
       self.browser.quit()

    def test_can_edit_entry(self) :
    
        self.browser.get('http://localhost:8000')
        time.sleep(1)
        
        interests = self.browser.find_element_by_id('uneditable_interests')
        edit = self.browser.find_element_by_id('edit_interests_button')
        
        self.assertEqual(interests.text, "Add interests")
        
        edit.click()
        time.sleep(1)
        
        editable_interests = self.browser.find_element_by_id('editable_interests')
        submit = self.browser.find_element_by_id('save_interests')
        
        self.assertEqual(editable_interests.text, "Add interests")
        
        editable_interests.click()
        editable_interests.clear()
        editable_interests.send_keys("WEB")
        
        submit.click()
        time.sleep(1)
        
        interests = self.browser.find_element_by_id('uneditable_interests')
        self.assertEqual(interests.text, "WEB")
        
class AwardsPageTest(unittest.TestCase):

    def setUp(self):
       self.browser = webdriver.Firefox()

    def tearDown(self):
       self.browser.quit()

    def test_can_add_and_edit_entry(self) :
    
        self.browser.get('http://localhost:8000')
        time.sleep(1)
        
        add_award = self.browser.find_element_by_id('add_award')
        add_award.click()
        time.sleep(1)
        
        new_award = self.browser.find_element_by_id('new_award_input')
        new_award.click()
        new_award.clear()
        new_award.send_keys('Google digital workshop')
        
        submit = self.browser.find_element_by_id('submit_award')
        submit.click()
        time.sleep(1)
        
        award = self.browser.find_element_by_id('uneditable_award_1')
        self.assertEqual(award.text, 'Google digital workshop Edit')
        
        edit = self.browser.find_element_by_id('edit_award_1')
        edit.click()
        time.sleep(1)
        
        award = self.browser.find_element_by_id('editable_award_input_1')
        award.click()
        award.clear()
        award.send_keys('Google digital workshop 2')
        
        submit = self.browser.find_element_by_id('save_award_1')
        submit.click()
        time.sleep(1)
        
        award = self.browser.find_element_by_id('uneditable_award_1')
        self.assertEqual(award.text, 'Google digital workshop 2 Edit')
        
        
        
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
