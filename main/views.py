from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import ShopBooks


#   def books(request):
#      ShopBooks_list = ShopBooks.objects.all()
#      return render(request, "books.html", {"ShopBooks_list": ShopBooks_list})


def books(request):
    ShopBooks_list = ShopBooks.objects.all()
    return render(request, "books.html", {"ShopBooks_list": ShopBooks_list})


def homepage(request):
    return render(request, "index.html")

def addup(request):
    return render(request, "addup.html")

def change(request):
    return render(request, "change.html")

def delet(request):
    return render(request, "delet.html")

def books(request):
    return render(request,"books.html")



def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})




def second(request):
    return HttpResponse("test 2 page")


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)


def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)