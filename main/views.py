from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse('Hello world') 
    # функция

def second(request):
    return HttpResponse('test2 page') 