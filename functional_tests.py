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

    def test_can_add_new_entry(self) :
    
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
        
        
        
#        {% for job in jobs %}
#        <div class="d-flex flex-column flex-md-row justify-content-between mb-5" id="uneditable_job_{{ job.id }}">
#            <div class="flex-grow-1">
#                <h3 class="mb-0" id="uneditable_job_title_{{ job.id }}" name="uneditable_job_title_{{ job.id }}">{{ job.title }}</h3>
#                <div class="subheading mb-3" id="uneditable_job_company_{{ job.id }}" name="uneditable_job_company_{{ job.id }}">{{ job.company }}</div>
#                <p id="uneditable_job_description_{{ job.id }}" name="uneditable_job_description_{{ job.id }}">{{ job.description }}</p>
#            </div>
#            <div class="flex-shrink-0"><span class="text-primary" id="uneditable_job_dates_{{ job.id }}" name="uneditable_job_dates_{{ job.id }}">{{ job.dates }}</span></div>
#        </div>
#
#        <div class="d-flex flex-column flex-md-row justify-content-between mb-5" id="editable_job_{{ job.id }}" style="display:none">
#            <div class="flex-grow-1">
#                <h3 class="mb-0" contenteditable="true" style="display:none" id="editable_job_title_{{ job.id }}" name="editable_job_title_{{ job.id }}">{{ job.title }}</h3>
#                <div class="subheading mb-3" contenteditable="true" style="display:none" id="editable_job_company_{{ job.id }}" name="editable_job_company_{{ job.id }}">{{ job.company }}</div>
#                <p contenteditable="true" style="display:none" id="editable_job_description_{{ job.id }}" name="editable_job_description_{{ job.id }}">{{ job.description }}</p>
#            </div>
#            <div class="flex-shrink-0"><span class="text-primary" contenteditable="true" id="editable_job_dates_{{ job.id }}" name="editable_job_dates_{{ job.id }}" style="display:none">{{ job.dates }}</span></div>
#            <p style="display:none" id="job_id_{{ job.id }}" name="job_id_{{ job.id }}">{{ job.id }}</p>
#        </div>
#
#        <button id="edit_experience_{{ job.id }}" onclick="
#            hideStuff('uneditable_job_title_{{ job.id }}');
#            hideStuff('uneditable_job_company_{{ job.id }}');
#            hideStuff('uneditable_job_description_{{ job.id }}');
#            hideStuff('uneditable_job_dates_{{ job.id }}');
#            hideStuff('edit_experience_{{ job.id }}');
#
#            showStuff('editable_job_title_{{ job.id }}');
#            showStuff('editable_job_company_{{ job.id }}');
#            showStuff('editable_job_description_{{ job.id }}');
#            showStuff('editable_job_dates_{{ job.id }}');
#            showStuff('submit_experience_{{ job.id }}')"> Edit job </button>
#
#        <button style="display:none" id="submit_experience_{{ job.id }}" onclick="
#            hideStuff('editable_job_title_{{ job.id }}');
#            hideStuff('editable_job_company_{{ job.id }}');
#            hideStuff('editable_job_description_{{ job.id }}');
#            hideStuff('editable_job_dates_{{ job.id }}');
#            hideStuff('submit_experience_{{ job.id }}');
#
#            showStuff('uneditable_job_title_{{ job.id }}');
#            showStuff('uneditable_job_company_{{ job.id }}');
#            showStuff('uneditable_job_description_{{ job.id }}');
#            showStuff('uneditable_job_dates_{{ job.id }}');
#            showStuff('edit_experience_{{ job.id }}');
#
#            addInput('editable_job_title_{{ job.id }}', 'edit_job_title');
#            addInput('editable_job_company_{{ job.id }}', 'edit_job_company');
#            addInput('editable_job_description_{{ job.id }}', 'edit_job_description');
#            addInput('editable_job_dates_{{ job.id }}', 'edit_job_dates');
#            addInput('job_id_{{ job.id }}', 'job_id');
#
#            clickButton('submit_edited_job');
#            "
#        > Submit </button>
#        {% endfor %}

if __name__ == '__main__':
    unittest.main(warnings='ignore')
