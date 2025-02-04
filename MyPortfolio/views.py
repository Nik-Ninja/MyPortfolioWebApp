from django.shortcuts import render


def goToHomePage(request):
    return render(request,'mainPage.html')