from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .models import TableKey
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


# Запрет на анонимных пользователей - обязательная аутентификация декоратором
@login_required(login_url="login")
# Получение данных из БД всех пользователей группы,залогиненого пользователя
def index(request):
    username = request.user
    users_in_group_1 = Group.objects.get(name="Group_1").user_set.all()
    users_in_group_2 = Group.objects.get(name="Group_2").user_set.all()
    users_in_group_admin = Group.objects.get(name="admin").user_set.all()

    if username in users_in_group_1:

        queryset = TableKey.objects.filter(name__in=users_in_group_1)
        context = {'TableKey': queryset}
        return render(request, "index.html", context)
    elif username in users_in_group_2:

        queryset = TableKey.objects.filter(name__in=users_in_group_2)
        context = {'TableKey': queryset}
        return render(request, "index.html", context)

    elif username in users_in_group_admin:

        queryset = TableKey.objects.all()
        context = {'TableKey': queryset}
        return render(request, "index.html", context)
    else:
         return HttpResponseNotFound("<h2>Password not found</h2>")

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

    # удаление данных из Бд

def delete(request, id):
    try:
        tablekey = TableKey.objects.get(id=id)
        tablekey.delete()
        return HttpResponseRedirect("/")
    except TableKey.DoesNotExist:
        return HttpResponseNotFound("<h2>Password not found</h2>")
