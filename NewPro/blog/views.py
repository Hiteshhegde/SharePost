from django.shortcuts import render
from .models import Post
from .forms import LoginForm

# Create your views here.

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def login(request):
    if request.method == "POST":
      #create form instacnce and populate with data from request
      form = LoginForm(request.POST)
      #check whether form data is valid
      if form.is_valid():
        #process the data in form.cleaned_data as required
        print(form)
        return HttpResponseRedirect('/home/')
    else:
      #create an empty form for the GET request
      form = LoginForm()
      context = {
	     'form':form
            }
    return render(request, 'blog/login.html', context=context)
