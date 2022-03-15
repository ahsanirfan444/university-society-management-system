from django.shortcuts import render, redirect
from django.core.mail import send_mail

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/console/admin/club/')
        elif request.user.is_staff:
            return redirect('/console/advisor/classrooms/')
        else:
            return redirect('/console/student/club/')
    else:
        return redirect('/accounts/login/')