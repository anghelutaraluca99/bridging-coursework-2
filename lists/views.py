from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import CV

def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('cv', ''),
    })
    
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
    return render(request, 'edit_experience.html')

def add_experience(request):
    return redirect('/')

def edit_education(request):
    return render(request, 'edit_education.html')

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
        print(name_surname)
    else:
        name_surname = 'NAME SURNAME'
        address = 'ADDRESS'
        email = 'email@email.com'
        about_description = 'Short Description'
        
    return render(request, 'home.html', {
        'name_surname': name_surname,
        'address': address,
        'email': email,
        'about_description': about_description,
    })
