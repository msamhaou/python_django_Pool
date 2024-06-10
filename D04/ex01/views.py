from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request=request, template_name='ex01/base.html')
def djan(request):
    return render(request=request, template_name='ex01/django.html')

def display(request):
    return render(request=request, template_name='ex01/display.html')

def templates(request):
    return render(request=request, template_name='ex01/templates.html')