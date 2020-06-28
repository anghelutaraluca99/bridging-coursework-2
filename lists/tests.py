from django.test import TestCase
from lists.models import CV, JOB, EDUCATION, INTERESTS, AWARDS

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

#   REMOVED TEST AS I'M CHANGING THE ARCHITECTURE OF THE WEBSITE

#class AboutPageTest(TestCase):
#
#    def test_uses_edit_about_template(self):
#        response = self.client.get('/edit_about')
#        self.assertTemplateUsed(response, 'edit_about.html')


class ExperiencePageTest(TestCase):

    def test_uses_edit_experience_template(self):
        response = self.client.get('/edit_experience')
        self.assertTemplateUsed(response, 'edit_experience.html')
        
class EducationPageTest(TestCase):

    def test_uses_edit_education_template(self):
        response = self.client.get('/edit_education')
        self.assertTemplateUsed(response, 'edit_education.html')
    
    
class SkillsPageTest(TestCase):

    def test_uses_edit_skills_template(self):
        response = self.client.get('/edit_skills')
        self.assertTemplateUsed(response, 'edit_skills.html')
    
    
class InterestsPageTest(TestCase):

    def test_uses_edit_experience_template(self):
        response = self.client.get('/edit_interests')
        self.assertTemplateUsed(response, 'edit_interests.html')
    
    
class AwardsPageTest(TestCase):

    def test_uses_edit_experience_template(self):
        response = self.client.get('/edit_awards')
        self.assertTemplateUsed(response, 'edit_awards.html')


class CVModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_item = CV()
        first_item.name_surname = 'Jane Doe'
        first_item.address = 'N/A'
        first_item.email = 'janedoe@email.com'
        first_item.about_description = 'N/A'
        first_item.save()

        second_item = CV()
        second_item.name_surname = 'John Doe'
        second_item.address = 'N/A'
        second_item.email = 'johndoe@email.com'
        second_item.about_description = 'N/A'
        second_item.save()

        saved_items = CV.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.name_surname, 'Jane Doe')
        self.assertEqual(second_saved_item.name_surname, 'John Doe')

class JOBModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_item = JOB()
        first_item.job_title = 'Front end developer'
        first_item.company = 'Google'
        first_item.job_description = 'N/A'
        first_item.job_dates = 'March 2019 - March 2020'
        first_item.save()

        second_item = JOB()
        second_item.job_title = 'Full stack developer'
        second_item.company = 'Apple'
        second_item.job_description = 'N/A'
        second_item.job_dates = 'March 2020 - Present'
        second_item.save()

        saved_items = JOB.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.job_title, 'Front end developer')
        self.assertEqual(first_saved_item.company, 'Google')
        self.assertEqual(first_saved_item.job_dates, 'March 2019 - March 2020')
        self.assertEqual(first_saved_item.job_description, 'N/A')
        self.assertEqual(second_saved_item.company, 'Apple')

class EDUCATIONModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_item = EDUCATION()
        first_item.institution = 'University of Birmingham'
        first_item.title = 'Computer Science'
        first_item.description = 'N/A'
        first_item.grade = '1st'
        first_item.dates = 'September 2018 - Present'
        first_item.save()

        second_item = EDUCATION()
        second_item.institution = 'CNGRC'
        second_item.title = 'MI'
        second_item.description = 'N/A'
        second_item.grade = '9.65'
        second_item.dates = 'September 2014 - June 2018'
        second_item.save()

        saved_items = EDUCATION.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        
        self.assertEqual(first_saved_item.institution, 'University of Birmingham')
        self.assertEqual(first_saved_item.title, 'Computer Science')
        self.assertEqual(first_saved_item.description, 'N/A')
        self.assertEqual(first_saved_item.grade, '1st')
        self.assertEqual(first_saved_item.dates, 'September 2018 - Present')
        
        self.assertEqual(second_saved_item.institution, 'CNGRC')
        self.assertEqual(second_saved_item.title, 'MI')
        self.assertEqual(second_saved_item.description, 'N/A')
        self.assertEqual(second_saved_item.grade, '9.65')
        self.assertEqual(second_saved_item.dates, 'September 2014 - June 2018')
        
class INTERESTSModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
    
        first_item = INTERESTS()
        first_item.description = 'N/A'
        first_item.save()
        
        second_item = INTERESTS()
        second_item.description = 'N/A2'
        second_item.save()
        
        saved_items = INTERESTS.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        
        self.assertEqual(first_saved_item.description, 'N/A')
        self.assertEqual(second_saved_item.description, 'N/A2')
        

class AWARDSModelTest(TestCase):
        
    def test_saving_and_retrieving_items(self):
    
        first_item = AWARDS()
        first_item.award = 'N/A'
        first_item.save()
        
        second_item = AWARDS()
        second_item.award = 'N/A2'
        second_item.save()
        
        saved_items = AWARDS.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        
        self.assertEqual(first_saved_item.award, 'N/A')
        self.assertEqual(second_saved_item.award, 'N/A2')
        
#    def test_can_save_a_POST_request(self):
#        self.client.post('/', data={'item_text': 'A new list item'})
#
#        self.assertEqual(Item.objects.count(), 1)
#        new_item = Item.objects.first()
#        self.assertEqual(new_item.text, 'A new list item')
#
#    def test_redirects_after_POST(self):
#        response = self.client.post('/', data={'item_text': 'A new list item'})
#        self.assertEqual(response.status_code, 302)
#        self.assertEqual(response['location'], '/')
#
#    def test_only_saves_items_when_necessary(self):
#        self.client.get('/')
#        self.assertEqual(Item.objects.count(), 0)
#
#    def test_displays_all_list_items(self):
#        Item.objects.create(text='itemey 1')
#        Item.objects.create(text='itemey 2')
#
#        response = self.client.get('/')
#
#        self.assertIn('itemey 1', response.content.decode())
#        self.assertIn('itemey 2', response.content.decode())
#
#
#class ItemModelTest(TestCase):
#
#    def test_saving_and_retrieving_items(self):
#        first_item = Item()
#        first_item.text = 'The first (ever) list item'
#        first_item.save()
#
#        second_item = Item()
#        second_item.text = 'Item the second'
#        second_item.save()
#
#        saved_items = Item.objects.all()
#        #test1
#        self.assertEqual(saved_items.count(), 2)
#
#        first_saved_item = saved_items[0]
#        second_saved_item = saved_items[1]
#        #tests 2 and 3
#        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
#        self.assertEqual(second_saved_item.text, 'Item the second')
