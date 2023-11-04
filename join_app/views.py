from django.shortcuts import render

def static_page(request):
    return render(request, 'join.html')
