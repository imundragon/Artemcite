from django.shortcuts import render




def index(request):
	about_site = "Наш Первый сайт"
	news = [
	"01.02 : Был создан сайт",
	"23.05 : Было создано меню",
	"12.06 : Добавлен блог",
	]
	return render(request,'index.html',
	{"about_site" : about_site,
	"news" : news })
# Create your viewЪs here.

def blogs(request):
	blogs = [
	{"id":1,"title":"Мой день","text":"..."},
	{"id":2,"title":"Моя школа","text":"..."},
	{"id":3,"title":"Моя кошка","text":"..."},
	]
	return render(request,'blogs.html',
	{"blogs" : blogs})
