from django.conf.urls import url, include
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url('edit_about', views.edit_about, name='edit_about'),
    url('edit_experience', views.edit_experience, name='edit_experience'),
    url('edit_education', views.edit_education, name='edit_education'),
    url('edit_skills', views.edit_skills, name='edit_skills'),
    url('edit_interests', views.edit_interests, name='edit_interests'),
    url('edit_awards', views.edit_awards, name='edit_awards'),
    
]
