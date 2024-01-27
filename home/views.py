from django.shortcuts import render
from .models import collaborator,facility, news, people, project, patent, publication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe

def index(request):
    return render(request,'home/index.html',{})

def about(request):
    return render(request,'home/about.html',{})

def academics(request):
    return render(request,'home/academics.html',{})

def director(request):
    return render(request,'home/director.html',{})

def facilities(request):
    return render(request,'home/facility.html', {'facilities':facility.objects.all()})

def ktc(request):
    return render(request,'home/ktc.html',{})

def kkp(request):
    return render(request,'home/kkp.html',{})

def sitemap(request):
    return render(request, 'home/sitemap.xml', content_type='text/xml')


def publications(request):
    temp = publication.objects.order_by('-yop')
    for t in temp:
        t.author = t.author.replace('Das B','<b>Das B</b>')
        t.author=mark_safe(t.author)
    # temp = temp.sort(temp.yop)
    return render(request,'home/publications.html',{'publications':temp})

def test(request):
    return render(request,'home/test.html')

def iec(request):
    return render(request,'home/iec.html')

def icscr(request):
    return render(request,'home/icscr.html')

def ibsc(request):
    return render(request,'home/ibsc.html')

def news_kavi(request):
    newss = news.objects.order_by('-date')
    return render(request,'home/news.html', {'newss':newss})

def contact(request):
    return render(request,'home/contact.html')

def collaborators(request):
    return render(request,'home/collaborators.html', {'collaborators':collaborator.objects.all()})

def faculty(request):
    return render(request,'home/faculty.html', {'faculty':people.objects.all()})

def patents(request):
    return render(request,'home/patent.html',{'patents':patent.objects.all()})

def projects(request):
    return render(request,'home/projects.html', {'projects':project.objects.all()})


def dashboard(request):
    if request.user.is_active:
        return render(request,'home/dashboard.html',
                              {'user_info':request.user,})
    else:
        return HttpResponse("<h1>You are not loggedin</h1>")

def admin_login(request):
    if request.user.is_active:
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('dashboard'))

                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")
        else:
            return render(request, 'home/login.html', {})


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('admin_login'))
