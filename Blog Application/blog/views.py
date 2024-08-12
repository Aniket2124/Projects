from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreatePostForm, RegistrationForm, ProfileForm
from .models import Post


# Create your views here.

def view_all_post(request):
    if request.user.is_authenticated:
        # Only show posts created by the logged-in user
        user_posts = Post.objects.filter(user=request.user)       
        return render(request, 'blog/posts.html', {'user_posts': user_posts})
    else:
        # Show all posts to unauthenticated users
        all_posts = Post.objects.all()
        return render(request, 'blog/posts.html', {'all_posts': all_posts})


def blog_detail(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=id, user= request.user)
        # post = Post.objects.get(id=id)
        return render(request, 'blog/post_detail.html', {'post': post})
    else:
        return redirect('login')


def blog_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreatePostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                    
                blog = Post.objects.create(title=title, content=content, user=request.user)
                # form.save()
                messages.success(request, 'Your post has been created successfully')
                return redirect('all_posts')
        else:
            form = CreatePostForm()
        return render(request, 'blog/blog_post.html', {'form':form})
    else:
        return redirect('login')
    

def update_blog(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        if request.method == 'POST':
            form = CreatePostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your post has been Updated successfully')
                return redirect('blog_detail', id=post.id)
        else:
            form = CreatePostForm(instance=post)
        return render(request, 'blog/update_blog.html', {'form':form})
    else:
        return redirect('login')


def delete_blog(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        post.delete()
        messages.success(request, 'Your post has been Deleted successfully')
        return redirect('all_posts')
    else:
        return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registred Successfully.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form':form})
    
def User_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! You are now logged in.')
            return redirect('all_posts')

            # user = authenticate(request, username=username, password=password)
            
        #     if user is not None:
        #         login(request, user)
        #         return redirect('all_posts')
        #     else:
        #         messages.error(request, 'Invalid username or password.')
        # else:
        #     form = AuthenticationForm()
        #     messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'blog/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You Have Logout successfully')
    return redirect('login')

def User_profile(request):
    data = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated successfully')
            return redirect('profile')
    else:
        form = ProfileForm(instance=data)
        return render(request, 'blog/profile.html', {'form': form})

