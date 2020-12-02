from django.shortcuts import render
from .models import *
from .forms import * 
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    return render(request, 'home.html')



def about_me(request):
    print(1)
    aboutme = AboutMe.objects.all()
    context = {'about_me':aboutme}
    return render(request, 'about_me.html', context)



def projects(request):
    n = 4
    projects = MyProject.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(projects,n)
    projects = paginator.page(page)
    context = {'projects':projects}
    return render(request, 'projects.html', context)


def projects_details(request, id):
    project = MyProject.objects.get(id = id)
    context = {'project':project}
    return render(request, 'project_details.html', context)


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        user = User.objects.create_user(username = username, password = password, first_name = first_name, last_name = last_name)
        form = SignupForm()
        message = "Your Successfully register"
        context = {'form':form, 'message':message}
        return render(request, 'signup.html', context)
    else:
        form = SignupForm()
        context = {'form':form}
        return render(request, 'signup.html', context)
