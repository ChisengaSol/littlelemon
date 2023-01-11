from django.shortcuts import render

# Create your views here.
# def menu(request):
#     menu_data = Menu.objects.all()
#     main_data = {"menu":menu_data}
#     return render(request,'menu.html',main_data)

def index(request):
    return render(request, 'index.html', {})

def home(request):
    return render(request, 'index.html', {})
