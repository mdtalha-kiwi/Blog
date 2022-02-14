from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def post(request):
    return render(request, 'post/index.html')
