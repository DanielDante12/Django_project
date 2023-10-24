from django.shortcuts import render
from django.http import HttpResponse

drinks = [
    {
    'mango juice',
    'lemonade',
    'orange juice'
    }
]
post =[
    {
    'author': 'Dante',
    'title': 'Love',
    'content': 'Love is a beautiful thing',
    'date': 'August 21, 2023'
    },
    {
      'author': 'John Doe',
    'title': 'Jealousy',
    'content': 'This is our second article',
    'date': 'August 28, 2023'  
    }
]
def home(request):
    
    context = {'post': post}
    return render(request,'blog/index.html', context)

def about(req):
    return render(req,'blog/about.html', {'title': 'About'})

def contactUs(req):
    return render(req, 'blog/contact.html')

def companyProfile(req):
    return render(req, 'blog/profile.html')