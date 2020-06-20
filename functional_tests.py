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

    def test_edit_buttons(self):
        self.browser.get('http://localhost:8000')
        time.sleep(1)
        
#        edit_about_button = self.browser.find_element_by_name("edit_about")
#        self.assertEqual(False, edit_about_button is None)
        
        edit_experience_button = self.browser.find_element_by_name("edit_experience")
        self.assertEqual(False, edit_experience_button is None)
        
        edit_education_button = self.browser.find_element_by_name("edit_education")
        self.assertEqual(False, edit_education_button is None)
        
        edit_skills_button = self.browser.find_element_by_name("edit_skills")
        self.assertEqual(False, edit_skills_button is None)
        
        edit_interests_button = self.browser.find_element_by_name("edit_interests")
        self.assertEqual(False, edit_interests_button is None)
        
        edit_awards_button = self.browser.find_element_by_name("edit_awards")
        self.assertEqual(False, edit_awards_button is None)
        

    def test_edit_submit_buttons(self):
        self.browser.get('http://localhost:8000')
        time.sleep(1)
        
        edit_about_button=self.browser.find_element_by_id("edit_about")
        submit_about_button = self.browser.find_element_by_id("submit_about")
        editable_about_div = self.browser.find_element_by_id("editable_about")
        uneditable_about_div = self.browser.find_element_by_id("uneditable_about")
        
        self.assertEqual(editable_about_div.value_of_css_property('display'), "none")
        self.assertEqual(uneditable_about_div.value_of_css_property('display'), "block")
        
        edit_about_button.click();
        time.sleep(1)
        
        editable_about_div = self.browser.find_element_by_id("editable_about")
        uneditable_about_div = self.browser.find_element_by_id("uneditable_about")
        
        self.assertEqual(editable_about_div.value_of_css_property('display'), "block")
        self.assertEqual(uneditable_about_div.value_of_css_property('display'), "none")
        
        submit_about_button.click();
        time.sleep(1)
        
        editable_about_div = self.browser.find_element_by_id("editable_about")
        uneditable_about_div = self.browser.find_element_by_id("uneditable_about")
        
        self.assertEqual(editable_about_div.value_of_css_property('display'), "none")
        self.assertEqual(uneditable_about_div.value_of_css_property('display'), "block")
        
        
#    def check_for_row_in_list_table(self, row_text):
#       table = self.browser.find_element_by_id('id_list_table')
#       rows = table.find_elements_by_tag_name('tr')
#       self.assertIn(row_text, [row.text for row in rows])
#
#    def test_can_start_a_list_and_retrieve_it_later(self):
#        # Edith has heard about a cool new online to-do app. She goes
#        # to check out its homepage
#        self.browser.get('http://localhost:8000')
#
#        # She notices the page title and header mention to-do lists
#        self.assertIn('To-Do', self.browser.title)
#        header_text = self.browser.find_element_by_tag_name('h1').text
#        self.assertIn('To-Do', header_text)
#
#        # She is invited to enter a to-do item straight away
#        inputbox = self.browser.find_element_by_id('id_new_item')
#        self.assertEqual(
#            inputbox.get_attribute('placeholder'),
#            'Enter a to-do item'
#        )
#
#        # She types "Buy peacock feathers" into a text box (Edith's hobby
#        # is tying fly-fishing lures)
#        inputbox.send_keys('Buy peacock feathers')
#
#        # When she hits enter, the page updates, and now the page lists
#        # "1: Buy peacock feathers" as an item in a to-do list table
#        inputbox.send_keys(Keys.ENTER)
#        time.sleep(1)
#        self.check_for_row_in_list_table('1: Buy peacock feathers')
#
#        # There is still a text box inviting her to add another item. She
#        # enters "Use peacock feathers to make a fly" (Edith is very
#        # methodical)
#        inputbox = self.browser.find_element_by_id('id_new_item')
#        inputbox.send_keys('Use peacock feathers to make a fly')
#        inputbox.send_keys(Keys.ENTER)
#        time.sleep(1)
#
#        # The page updates again, and now shows both items on her list
#        self.check_for_row_in_list_table('1: Buy peacock feathers')
#        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
#
#        # Edith wonders whether the site will remember her list. Then she sees
#        # that the site has generated a unique URL for her -- there is some
#        # explanatory text to that effect.
#        self.fail('Finish the test!')
#
#        # She visits that URL - her to-do list is still there.
#
#        # The page updates again, and now shows both items on her list
#        [...]

if __name__ == '__main__':
    unittest.main(warnings='ignore')
