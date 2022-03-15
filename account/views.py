import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.mail import send_mail
from .serializers import UserSeriaizer
from random import randint

def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    logout = False
    if request.method == 'GET':
        if request.GET.get('log_out_by_user') == '1':
            logout = True

    if request.method == 'POST':
        body = json.loads(request.body)
        username = body['username']
        password = body['password']
        user=User.objects.filter(username=username).first()
        if user:
            auth_user = authenticate(request, username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return JsonResponse({'status': 200}, status=200)
            else:
                u=User.objects.filter(username=username).first()
                if u:
                    u.profile.failed_attempt = u.profile.failed_attempt  + 1
                    if u.profile.failed_attempt > 3:
                        u.profile.failed_attempt = 0
                        send_mail('subject', 'Unusual login atempt detected on your APUClub account', 'Your_Email_Address', [u.email])
                    u.save()
                return JsonResponse({'status': 404}, status=404)
        else:
            return JsonResponse({'status': 404}, status=404)
    
    context = {
        'logout': logout
    }

    return render(request, 'account/login.html', context)

def change(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if request.method == 'POST':
        body = json.loads(request.body)
        current_pass = body['current_pass']
        new_pass = body['new_pass']
        send_code = body['code']
        otp = body['otp']
        if request.user.check_password(current_pass):
            if send_code == '1':
                code = randint(10000, 99999)
                print(code)
                send_mail('subject', 'Your APUClub account verification code for passwod change is: '+ str(code), 'Your_Email_Address', [request.user.email])
                return JsonResponse({'status': 200, 'code': code}, status=200)
            elif (str(send_code) == str(otp)):
                request.user.set_password(new_pass)
                request.user.save()
                return JsonResponse({'status': 201}, status=201)
            else:
                return JsonResponse({'status': 405}, status=405)
        else:
            return JsonResponse({'status': 404}, status=404)

    context = {

    }
    return render(request, 'account/change.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

        
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            first_name = body['first_name']
            last_name = body['last_name']
            username = body['username']
            email = body['email']
            password = body['password']
            actype = body['actype']
            has_already = User.objects.filter(username=str(username)).first()
            if has_already:
                return JsonResponse({'status': 409}, status=409)
            else:
                code = randint(10000, 99999)
                send_mail('subject', 'Your APUClub account verification code is: '+ str(code), 'Your_Email_Address', [email])
                new_user = User.objects.create_user(username, email, password)
                new_user.profile.verify_code = code
                new_user.first_name = first_name
                new_user.last_name = last_name

                if actype =='1':
                    new_user.is_staff = True
                    new_user.is_admin = True
                    new_user.is_superuser = True
                elif actype == '2':
                    new_user.is_staff = True
                elif actype == '3':
                    pass
                new_user.save()
                login(request, new_user)
                return JsonResponse({'status': 201}, status=201)
        except ValueError:
            pass
    return render(request, 'account/signup.html')


def verify(request):
    if request.user.is_authenticated:
        if not request.user.profile.is_email_verified:
            pass
        else:
            return redirect('/')

    if request.POST.get('verify'):
        if str(request.user.profile.verify_code) == request.POST.get('verify'):
            request.user.profile.is_email_verified = True
            request.user.save()
            return redirect('/')
    
    return render(request, 'account/verify.html')

def accounts(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        pass
    return render(request, 'account/accounts.html')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/accounts/login/?log_out_by_user=1')
    else:
        return redirect('/accounts/login/')