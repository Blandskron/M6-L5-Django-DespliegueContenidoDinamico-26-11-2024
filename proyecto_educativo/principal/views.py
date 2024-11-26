from django.shortcuts import render

def nombre(request):
    return render(request, 'index.html')
