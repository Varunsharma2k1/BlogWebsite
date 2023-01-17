from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import blog
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    # my_blogs=get_object_or_404(blog,pk=1)
    my_blogs=blog.objects.all()
    p = Paginator(my_blogs,3)
    page = request.GET.get('page')
    page_obj = p.get_page(page)
   
    return render (request,'myblog/index.html',{'blog': my_blogs, 'page_obj':page_obj})

def article(request,blog_id):
    my_blogs=get_object_or_404(blog,pk=blog_id)
    return render(request,'myblog/article.html',{'blog':my_blogs})

