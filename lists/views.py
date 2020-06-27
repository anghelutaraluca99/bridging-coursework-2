from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import CV, JOB, EDUCATION, INTERESTS, AWARDS
    
def edit_about(request):
    if request.method == 'POST':
        name_surname = request.POST.get('name_surname_input', "")
        address = request.POST.get('address_input', "")
        email = request.POST.get('email_input', "")
        about_description = request.POST.get('about_description_input', "")
            
        cv = CV.objects.all()
        
        if len(cv) == 0:
            cv = CV(name_surname = name_surname, address = address, email = email, about_description = about_description)
            cv.save()
        else :
            cv[0].name_surname = name_surname
            cv[0].address = address
            cv[0].email = email
            cv[0].about_description = about_description
            cv[0].save()
        return redirect('/')
    
def edit_experience(request):
    if request.method == 'POST':
        id = request.POST.get('job_id', "")
        title = request.POST.get('edit_job_title', "")
        company = request.POST.get('edit_job_company', "")
        description = request.POST.get('edit_job_description', "")
        dates = request.POST.get('edit_job_dates', "")
        
        job = JOB.objects.get(id = id)
        job.title = title
        job.company = company
        job.description = description
        job.dates = dates
        job.save()
        
    return redirect('/')

def add_experience(request):
    if request.method == 'POST':
        title = request.POST.get('new_job_title', "")
        company = request.POST.get('new_job_company', "")
        description = request.POST.get('new_job_description', "")
        dates = request.POST.get('new_job_dates', "")
        
        job = JOB(title=title, company=company, description=description, dates=dates)
        job.save()
    return redirect('/')
    
def add_education(request):
    if request.method == 'POST':
        school = request.POST.get('new_school', "")
        qualification = request.POST.get('new_qualification', "")
        description = request.POST.get('new_education_description', "")
        grade = request.POST.get('new_grade', "")
        dates = request.POST.get('new_education_dates', "")

        ed = EDUCATION(school=school, qualification=qualification, description=description, grade=grade, dates=dates)
        ed.save()
    return redirect('/')

def edit_education(request):
    if request.method == 'POST':
        id = request.POST.get('ed_id', "")
        school = request.POST.get('edit_school', "")
        qualification = request.POST.get('edit_qualification', "")
        description = request.POST.get('edit_education_description', "")
        grade = request.POST.get('edit_education_grade', "")
        dates = request.POST.get('edit_education_dates', "")

        print(id)
        print(school)
        print(qualification)
        print(description)
        print(grade)
        print(dates)

        ed = EDUCATION.objects.get(id = id)
        ed.school = school
        ed.qualification = qualification
        ed.description = description
        ed.grade = grade
        ed.dates = dates
        ed.save()
    return redirect('/')

def edit_skills(request):
    return render(request, 'edit_skills.html')

def edit_interests(request):
    if request.method == 'POST':
        description = request.POST.get('edit_interests', "")
        interests = INTERESTS.objects.all()[0]
        interests.description = description
        interests.save()
    return redirect('/')

def edit_awards(request):
    if request.method == 'POST':
        award = request.POST.get('edit_award', "")
        id = request.POST.get('award_id', "")
        print(award)
        print(id)
        aw = AWARDS.objects.get(id=id)
        aw.award = award
        aw.save()
    return redirect('/')


def add_awards(request):
    if request.method == 'POST':
        award = request.POST.get('new_award', "")
        award = AWARDS(award=award)
        award.save()
    return redirect('/')

def home_page(request):
    
    if len(CV.objects.all()) == 0:
        name_surname = 'NAME SURNAME'
        address = 'ADDRESS'
        email = 'email@email.com'
        about_description = 'Short Description'
        cv = CV(name_surname=name_surname, address=address, email=email, about_description=about_description)
        cv.save()
    
    if len(INTERESTS.objects.all()) == 0 :
        description = 'Add interests'
        interests = INTERESTS(description = description)
        interests.save()
    
    cv = CV.objects.all()[0]
    jobs = JOB.objects.all()
    education = EDUCATION.objects.all()
    interests = INTERESTS.objects.all()[0]
    awards = AWARDS.objects.all()
    
    return render(request, 'home.html', {
        'cv' : cv,
        'jobs': jobs,
        'education' : education,
        'interests' : interests,
        'awards' : awards,
    })
