from django.shortcuts import render



def index(request):
    return render(request, 'core/main_page.html')
