from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import djangoClasses


def admin_console(request):
    classes = djangoClasses.objects.all()
    return render(request, 'home.html', {'classes': classes})


