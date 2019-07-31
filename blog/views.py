from django.shortcuts import render,redirect
from .models import Blog

# Create your views here.
def home(req):
    one_blog=Blog.objects
    return render(req,'home.html',{'blogs':one_blog})

def new(req):
    return render(req,'new.html')

def create(req):
    one_blog=Blog()
    one_blog.title=req.POST['title']
    one_blog.content=req.POST['content']
    if 'image' in req.FILES.keys():
        new_memo.image=req.FILES['image']
    one_blog.save()
    return redirect('/')
