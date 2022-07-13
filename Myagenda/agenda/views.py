# Create your views here.
# views dosyası, sınıfların ve metotların çalıştırıldığı yerdir.
from django.shortcuts import render, redirect
# render() metodu, templates oluşturulduğunda kullanılan metottur.
from django.http import HttpResponse 
# http ve HttpResponse(), templates yok iken yani html ile çıktı verilmeyecekse
#  kullanılan kütüphane ve sınıftır.
from .models import Todos
from .forms import ListForm


def homepage(request): # İlk parametre her zaman request'tir.
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            newtodo = Todos.objects.all() # Todos'taki bütün objeleri getirir.
            return render(request,"agenda/home",{"todo_list":newtodo}) 
    else: 
        newtodo = Todos.objects.all() # Todos'taki bütün objeleri getirir.
        return render(request,"agenda/home",{"todo_list":newtodo}) 
    # Burada templates klasöründeki tanımladığımız çeşitli uygulamalar var ise onların içinde 
    # bulunan html dosyalarını getirmek için tanımlama yapılır.
    ## Burada sözlük içerisindeki todo_list key'ini Jinja Template ile home html sayfasında çağırabiliriz.
def developer(request):
    return render(request,"agenda/developer")
def create(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            newtodo = Todos.objects.all() # Todos'taki bütün objeleri getirir.
            return render(request,"agenda/create",{"todo_list":newtodo}) 
    else: 
        newtodo = Todos.objects.all() # Todos'taki bütün objeleri getirir.
        return render(request,"agenda/create",{"todo_list":newtodo}) 
    
def about(request):
    return render(request,"agenda/about") 
"""
def about(request):
    return render(request,"agenda/about", {"name":"Yasin Ramazan GÖK"}) 
    # Burada sözlük içerisinde yazılan key-value ifadelerini örneğin 
    # bu metodun gösterdiği about sayfasında kullanmak için Jinja Template kullanılır.
    # Buradaki Jinja Template kullanım örneği değişken çağırmadır.
    # def about(request):
    #     isim="Yasin Ramazan GÖK"
    #     return render(request,"agenda/about", {"name":isim}) şeklinde de kullanılabilir.
"""
def delete(request,Todos_id):
    todo = Todos.objects.get(pk = Todos_id)
    todo.delete()
    return redirect("home")
def yes_finish(request,Todos_id):
    todo = Todos.objects.get(pk = Todos_id)
    todo.finished=False
    todo.save()
    return redirect("home")
def no_finish(request,Todos_id):
    todo = Todos.objects.get(pk = Todos_id)
    todo.finished=True
    todo.save()
    return redirect("home")
def update(request,Todos_id):
    if request.method == "POST":
        todooo = Todos.objects.get(pk=Todos_id)
        form = ListForm(request.POST or None, instance=todooo)
        if form.is_valid:
            form.save()
            return redirect("home")

    else:    
        todo_list = Todos.objects.all()
        return render(request,"agenda/update",{"todo_list":todo_list})

