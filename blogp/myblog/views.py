from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import blog

# Create your views here.
def home(request):
    # my_blogs=get_object_or_404(blog,pk=1)
    my_blogs=blog.objects.all()
   
    return render (request,'myblog/index.html',{'blog': my_blogs},)

def article(request,blog_id):
    my_blogs=get_object_or_404(blog,pk=blog_id)
    return render(request,'myblog/article.html',{'blog':my_blogs})

