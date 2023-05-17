from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    context = {
        "data": "Jalaj",
        "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return render(request, "app/xyz.html", context)
