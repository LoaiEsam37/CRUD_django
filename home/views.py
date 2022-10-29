from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import USERS

def HomePage(request):
    users = USERS.objects.all().order_by('firstname').values()
    context = {}
    context["users"] = users
    return render(request, "homepage.html", context)

def Add(request):

    if request.method == "GET":
        return render(request, "add.html")

    if request.POST['firstname'] == "" or request.POST['lastname'] == "":
        context = {}
        context['empty'] = True
        return render(request, "add.html", context)

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    user = USERS.objects.create(firstname=firstname, lastname=lastname)
    user.save()

    return HttpResponseRedirect(reverse('homepage'))

def Delete(request, id):

    user = USERS.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('homepage'))

def Update(request, id):
    if request.method == "POST":
        if request.POST['firstname'] == "" or request.POST['lastname'] == "":
            user = USERS.objects.get(id=id)
            context = {}
            context["empty"] = True
            context["myuser"] = user
            return render(request, "update.html", context)
            
        user = USERS.objects.get(id=id)
        user.firstname = request.POST['firstname']
        user.lastname = request.POST['lastname']
        user.save()
        return HttpResponseRedirect(reverse('homepage'))

    user = USERS.objects.get(id=id)
    context = {}
    context["myuser"] = user
    return render(request, "update.html", context)