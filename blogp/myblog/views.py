from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import blog
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # my_blogs=get_object_or_404(blog,pk=1)
    my_blogs=blog.objects.all()
    p = Paginator(my_blogs,3)
    page = request.GET.get('page')
    page_obj = p.get_page(page)
   
    return render (request,'myblog/index.html',{'blog': my_blogs, 'page_obj':page_obj})

@login_required(login_url='ll')
def article(request,blog_id):
    my_blogs=get_object_or_404(blog,pk=blog_id)
    return render(request,'myblog/article.html',{'blog':my_blogs})

def nav(request):
    return render(request,'myblog/nav.html')

def ll(request):
    if request.method=='GET':
        form= AuthenticationForm()
        return render(request,'myblog/LL.html',{'form':form})
    else:
        uname=request.POST['username']
        upwd=request.POST['password']
        user = authenticate(request,username=uname,password=upwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'myblog/LL.html',{'form':AuthenticationForm(), 'message':'user not found'})

def ss(request):
    if request.method=='GET':
        form=UserCreationForm()
        return render(request,'myblog/ss.html',{'form':form})
    else:    
        uname=request.POST['username']
        upwd1=request.POST['password1']
        upwd2=request.POST['password2']
        print(uname)
        if upwd1==upwd2:
            try:
                user=User.objects.create_user(username=uname,password=upwd2)
                user.save()
                # login(request,user)
            except IntegrityError:
                return render(request,'myblog/ss.html',{'form':UserCreationForm(),'message':'Username already exist'})
            else:
                return redirect('home')
        else:
            return render(request,'myblog/ss.html',{'form':UserCreationForm(),'message':'Password mismatch error'})

def logoutuser(request):
    logout(request)
    return redirect('home')
