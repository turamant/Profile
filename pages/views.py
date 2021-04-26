from django.shortcuts import render

# Create your views here.

def links_view(request):
    return render(request,'links.html')

def resume_view(request):
    return render(request,'resume.html')

def base_view(request):
    return render(request, '_base.html')


