from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .models import TableKey
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from cryptography.fernet import Fernet

class Crypto:

        def create_key(self):
          key = Fernet.generate_key()

        def encrypt(data,key):
          f = Fernet(key)
          f.encrypt(b"")
          return f.encrypt(b"")

        def decrypt(data,key):
          f = Fernet(key)
          f.decrypt(f.encrypt(b""))
          return f.decrypt(f.encrypt(b""))

 # Функция на ошибку 404
def error404(request):
    username = request.user

    for a in Group.objects.all():
        users_in_group = Group.objects.get(name=a.name).user_set.all()
        if username not in users_in_group:
            return render(request, "error404.html")

# Запрет на анонимных пользователей - обязательная аутентификация декоратором
@login_required(login_url="login")
# Получение данных из БД всех пользователей группы,залогиненого пользователя
def index(request):
    username = request.user

    for a in Group.objects.all():
        users_in_group = Group.objects.get(name=a.name).user_set.all()
        if username in users_in_group:
            if username.__str__() == "admin":
                return render(request, "index.html", {'TableKey': TableKey.objects.all()})
            return render(request, "index.html", {'TableKey': TableKey.objects.filter(name__in=users_in_group)})
    else:
        return HttpResponseRedirect("error404")

    # Сохранение данных в БД пользователем
def user_create(request):
    if request.method == "POST":
        TableKey.objects.get_or_create(name=request.user, forWhat=request.POST.get("forWhat"),
                                       password=request.POST.get("password"),specification=request.POST.get("specification"),
                                       published_date=request.POST.get("published_date"))

    return render(request, "user_create.html")

    # Изменение данных в БД Пользователем

def edit(request, id):
    try:
        tablekey = TableKey.objects.get(id=id)

        if request.method == "POST":
            tablekey.name = User.objects.get(username=request.user)
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

    # удаление данных из Бд

def delete(request, id):
    try:
        tablekey = TableKey.objects.get(id=id)
        tablekey.delete()
        return HttpResponseRedirect("/")
    except TableKey.DoesNotExist:
        return HttpResponseNotFound("<h2>Password not found</h2>")

