from django.http import HttpResponseRedirect
from django.shortcuts import redirect,render,get_object_or_404
from .forms import PostForm,CommentForm
from .models import Post,PostView
from django.contrib.auth.decorators import login_required
from blog.models import Comment, Like, Post, PostView



def post_add(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post =  form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    context = {
        'form':form
    }

    return render(request, 'blog/blog_add.html', context)

def blog_detail(request, slug): 
    post =  Post.objects.get(slug=slug)
    comment_form=CommentForm()
    new_comment = None
    comment_list=Comment.objects.filter(post=post)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            return redirect('detail', slug=slug)

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)

    context = {
        'post':post,
        'new_comment': new_comment,
        'comment_form':comment_form,
        'comment_list':comment_list
    }
    return render(request, 'blog/blog_detail.html', context)






def home(request):
    posts=Post.objects.all()
    context={'posts':posts}

    return render(request, 'home.html',context)

def blog_update(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    context = {
        "form" : form
    }
    return render(request, "blog/blog_update.html", context)
def blog_delete(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == "POST":
        post.delete()
        return redirect("home")
    
    context = {
        'post':post
    }
    
    return render(request, "blog/blog_delete.html", context)

    

    
def likeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    Like.objects.get_or_create(user=request.user, post=post)
    context = {
        'post':post,
        
    }
    return render(request, 'blog/blog_detail.html', context)

