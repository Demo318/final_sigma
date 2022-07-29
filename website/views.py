from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from website.models import Post

def index(request):
  context = {}
  posts = Post.objects.all().order_by('-date_created')
  context['posts'] = posts
  for post in context['posts']:
    post.body = post.body[0:300] + "..."
  return render(request, 'website/index.html', context=context)


def show_post(request, post_title_slug):
  context = {}
  try:
    post = Post.objects.get(slug=post_title_slug)
    context['post'] = post
  except Post.DoesNotExist:
    return redirect('/')
  return render(request, 'website/post.html', context=context)


# TODO: Add password-reset feature https://ordinarycoders.com/blog/article/django-password-reset
def register_request(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, "Registration successful.")
      return redirect("website:index")
    messages.error(request, "Unsuccessful registration. Invalid information.")
  form = NewUserForm()
  return render(request=request, template_name="website/register.html", context={ "register_form":form })


def login_request(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect("website:index")
      else:
        messages.error(request, "Invalid username or password.")
    else:
      messages.error(request, "Invalid username or password.")
  form = AuthenticationForm()
  return render(request=request, template_name="website/login.html", context={"login_form":form})


def logout_request(request):
  logout(request)
  messages.info(request, "You have successfully logged out.")
  return redirect("website:index")
