from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from .models import TableKey
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def index(request):

    # Получение данных из БД
    queryset = TableKey.objects.all()

    context = {'TableKey': queryset}
    return render(request, "index.html", context)

    # Сохранение данных в БД пользователем
def user_create(request):
    if request.method == "POST":
        tablekey = TableKey()
        tablekey.name = User.objects.get(username=request.POST.get("name"))
        tablekey.forWhat = request.POST.get("forWhat")
        tablekey.password = request.POST.get("password")
        tablekey.specification = request.POST.get("specification")
        tablekey.published_date = request.POST.get("published_date")
        tablekey.save()
    #return HttpResponseRedirect("/")
    return render(request, "user_create.html")


        # Изменение данных в БД Пользователем
def edit(request, id):
    try:
        tablekey = TableKey.objects.get(id=id)

        if request.method == "POST":
            tablekey.name = User.objects.get(username=request.POST.get("name"))
            tablekey.forWhat = request.POST.get("forWhat")
            tablekey.password = request.POST.get("password")
            tablekey.specification = request.POST.get("specification")
            tablekey.published_date = request.POST.get("published_date")
            tablekey.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"tablekey": tablekey})
    except TableKey.DoesNotExist:
        return HttpResponseNotFound("<h2>Password not found</h2>")

    # удаление данных из бд
def delete(request, id):
        try:
            tablekey = TableKey.objects.get(id=id)
            tablekey.delete()
            return HttpResponseRedirect("/")
        except TableKey.DoesNotExist:
            return HttpResponseNotFound("<h2>Password not found</h2>")





