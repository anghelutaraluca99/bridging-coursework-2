from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
    
def edit_about(request):
    return render(request, 'edit_about.html')
    
def edit_experience(request):
    return render(request, 'edit_experience.html')

def edit_education(request):
    return render(request, 'edit_education.html')

def edit_skills(request):
    return render(request, 'edit_skills.html')

def edit_interests(request):
    return render(request, 'edit_interests.html')

def edit_awards(request):
    return render(request, 'edit_awards.html')

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
