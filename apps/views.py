from django.shortcuts import render, redirect
from .forms import (ContactForm,
                    UserProjectsForm,
                    # UserResume,
                    )
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == "POST":
        form =  ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            data = ContactToUser(name = cd['name'],email = cd['email'], contact_phone = cd['contact_phone'], 
                                message = cd['message'])
            data.save()
            messages.success(request,"Thank you for contacting with me, I will be in touch within 24 hours")

            return redirect('Home')
    else:
        form = ContactForm()
                              #
    ProjectData = UserProjects.objects.all()
    data = Owner.objects.all()
    resume = UserResume.objects.all()

    return render(request,'index.html',{
                                        'form':form,
                                        "projectsdata":ProjectData,
                                        'data':data,
                                        'resume':resume,
                                        })

def userprojects(request):
    if request.method == "POST":
        form = UserProjectsForm(request.POST,  request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            data = UserProjects(name = cd['name'], description= cd['description'],
                                github_link = cd['github_link'], project_picture = cd["project_picture"])
            data.save()
            return redirect('/project')
    else:
        form = UserProjectsForm()
    ProjectData = UserProjects.objects.all()
    return render(request,'projects.html',{'userprojects':form,"projectsdata":ProjectData})

def ownerdetail(request):
    data = Owner.objects.all()
    return render(request,'index.html',{
                                        'data':data,
                                        })