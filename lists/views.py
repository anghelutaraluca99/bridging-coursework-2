from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import CV, JOB, EDUCATION
    
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
    return render(request, 'edit_interests.html')

def edit_awards(request):
    return render(request, 'edit_awards.html')

def home_page(request):
    
    if len(CV.objects.all()) > 0:
        cv = CV.objects.all()[0]
        name_surname = cv.name_surname
        address = cv.address
        email = cv.email
        about_description = cv.about_description
    else:
        name_surname = 'NAME SURNAME'
        address = 'ADDRESS'
        email = 'email@email.com'
        about_description = 'Short Description'
    
    jobs = JOB.objects.all()
    education = EDUCATION.objects.all()
        
    return render(request, 'home.html', {
        'name_surname': name_surname,
        'address': address,
        'email': email,
        'about_description': about_description,
        'jobs': jobs,
        'education' : education,
    })
