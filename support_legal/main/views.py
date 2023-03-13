from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import RegisterFrom
from .forms import PostForm

# Create your views here.
def post_list(req):
    posts = Post.objects.all()

    if req.method == "POST":
        post_id = req.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == req.user:
            post.delete()
    return render(req, "main/post_list.html", {"post_list": posts})

def post_detail(req, post_id):
    post = Post.objects.get(pk=post_id)
    return render(req, "main/post_detail.html", {"post_detail":post})

@login_required(login_url="/login")
def create_post(req):
    if req.method == "POST":
        form = PostForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = req.user
            post.save()
            return redirect("/post_list")
    else:
            form = PostForm()
    return render(req, "main/create_post.html", {"form": form})

@login_required(login_url="/login")
def update_post(req, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(req.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("/post_list")
    return render(req, "main/post_update.html", {"post": post, 'form':form})
    
def sign_up(req):
    if req.method == "POST":
        form = RegisterFrom(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect("/post_list")
    else:
        form = RegisterFrom()
    return render(req, "registration/sign_up.html", {"form": form}) 


