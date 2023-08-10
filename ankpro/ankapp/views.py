from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_view(request):
    return HttpResponse('hii this is ank')

def main_index(request):
    return render(request, 'ankapp/index.html')
def main_contact(request):
    return render(request, 'ankapp/contact.html')
def main_home(request):
    return render(request, 'ankapp/home1.html')
def main_about(request):
    return render(request, 'ankapp/about.html')

