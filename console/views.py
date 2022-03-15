from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.db.models import Q

def admin_console(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')


    if not request.user.is_superuser:
        return redirect('/')


    context = {
        
    }
    return render(request, 'console/admin.html', context)


def admin_club(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')



    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')


    if not request.user.is_superuser:
        return redirect('/')


    if request.method == 'POST':
        if request.POST.get('club_name') and request.POST.get('club_des') and request.POST.get('club_approved'):
            c=Club.objects.create(
                user=request.user,
                name = request.POST.get('club_name'),
                description = request.POST.get('club_des'),
            )
            c.approved = True if request.POST.get('club_approved') == '1' else False
            c.save()

            return redirect('/console/admin/club/')

    if request.method == 'GET' and request.GET.get('delete'):
        has_club = Club.objects.filter(id=request.GET.get('delete')).first()
        if has_club:
            has_club.delete()
            return redirect('/console/admin/club/')

    if request.GET.get('toggle_member'):
        has_member = ClubMember.objects.filter(id=request.GET.get('toggle_member')).first()
        if has_member:
            if has_member.status:
                has_member.status = False
            else:
                has_member.status = True
            has_member.save()

        return redirect('/console/admin/club/')
    
    if request.GET.get('delete_member'):
        has_member = ClubMember.objects.filter(id=request.GET.get('delete_member')).first()
        if has_member:
            has_member.delete()
        return redirect('/console/admin/club/')

    clubs = Club.objects.all().order_by('-id')
    members = ClubMember.objects.all().order_by('-id')
    context = {
        'clubs': clubs,
        'members': members,
    }
    return render(request, 'console/admin-club.html', context)


def admin_classrooms(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')


    if not request.user.is_superuser:
        return redirect('/')


    if request.method == 'POST':
        if request.POST.get('classroom_name') and request.POST.get('classroom_number') and request.POST.get('classroom_link'):
            if request.POST.get('book_to'):
                has_staff = User.objects.filter(id=request.POST.get('book_to'), is_staff=True, is_superuser=False).first()
                if has_staff:
                    c=Classroom.objects.create(
                        user=request.user,
                        book_to=has_staff,
                        book_date = datetime.now(),
                        name = request.POST.get('classroom_name'),
                        room = request.POST.get('classroom_number'),
                        link = request.POST.get('classroom_link'),
                    )
            else:
                c=Classroom.objects.create(
                    user=request.user,
                    name = request.POST.get('classroom_name'),
                    room = request.POST.get('classroom_number'),
                    link = request.POST.get('classroom_link'),
                )
            return redirect('/console/admin/classrooms/')
    
    if request.GET.get('delete'):
        has_booking = Classroom.objects.filter(id=request.GET.get('delete'))
        if has_booking:
            has_booking.delete()
        return redirect('/console/admin/classrooms/')

    advisors = User.objects.filter(is_staff=True, is_superuser=False).order_by('-id')
    classroom = Classroom.objects.all().order_by('-id')
    context = {
        'advisors': advisors,
        'classroom': classroom,
    }
    return render(request, 'console/admin-classrooms.html', context)


def admin_events(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if not request.user.is_superuser:
        return redirect('/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')


    if request.method == 'POST':
        if request.POST.get('event_title') and request.POST.get('event_des') and request.POST.get('club'):
            has_club = Club.objects.filter(id=request.POST.get('club')).first()
            if has_club:
                e=Event.objects.create(
                    user=request.user,
                    club=has_club,
                    title = request.POST.get('event_title'),
                    description = request.POST.get('event_des'),
                    status = True,
                )
            return redirect('/console/admin/events/')

    if request.method == 'GET' and request.GET.get('delete'):
        has_event = Event.objects.filter(id=request.GET.get('delete')).first()
        if has_event:
            has_event.delete()
            return redirect('/console/admin/events/')

    if request.GET.get('toggle_status'):
        has_event = Event.objects.filter(id=request.GET.get('toggle_status')).first()
        if has_event:
            if has_event.status:
                has_event.status = False
            else:
                has_event.status = True
            has_event.save()
            


    clubs = Club.objects.all().order_by('-id')
    events = Event.objects.all().order_by('-id')
    context = {
        'clubs': clubs,
        'events': events,
    }
    return render(request, 'console/admin-events.html', context)


def admin_enquiries(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')


    if not request.user.is_superuser:
        return redirect('/')

    

    if request.method == 'POST':
        if request.POST.get('a') and request.POST.get('id'):
            e = Enquiry.objects.filter(id=request.POST.get('id')).first()

            if e:
                e.answer = request.POST.get('a')
                e.replyer = request.user

                e.save()
            return redirect('/console/admin/student-enquiries/')


    enquiries = Enquiry.objects.all().order_by('-id')

    context = {
        'enquiries': enquiries
    }
    return render(request, 'console/admin-enquiries.html', context)

def admin_manage_users(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')
    

    if not request.user.is_superuser:
        return redirect('/')


    if request.GET.get('delete'):
        has_user = User.objects.filter(id=request.GET.get('delete')).first()
        if has_user:
            has_user.delete()
            return redirect('/console/admin/manage-users/')

    if request.GET.get('toggle_status'):
        has_user = User.objects.filter(id=request.GET.get('toggle_status')).first()
        if has_user:
            if has_user.is_active:
                has_user.is_active = False
            else:
                has_user.is_active = True
            has_user.save()
        return redirect('/console/admin/manage-users/')

    users = User.objects.all().order_by('-id').exclude(username=request.user.username)
    context = {
        'users': users,
    }
    return render(request, 'console/admin-manage-users.html', context)








# advisor
def advisor_console(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')


    if not request.user.is_staff or request.user.is_superuser:
        return redirect('/')

    context = {
        
    }
    return render(request, 'console/advisor.html', context)


def advisor_classrooms(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    
    if not request.user.is_staff or request.user.is_superuser:
        return redirect('/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if request.GET.get('remove'):
        has_room = Classroom.objects.filter(id=request.GET.get('remove'), book_to=request.user).first()
        if has_room:
            has_room.book_to=None
            has_room.book_date=None
            has_room.save()
            return redirect('/console/advisor/classrooms/')

    if request.GET.get('request'):
        has_room = Classroom.objects.filter(id=request.GET.get('request'), book_to=None).first()
        if has_room:
            has_room.book_to=request.user
            has_room.book_date = datetime.now()
            has_room.save()

    classroom = Classroom.objects.filter(Q(book_to=request.user)|Q(book_to=None)).order_by('-id')

    context = {
        'classroom': classroom,
    }
    return render(request, 'console/advisor-classroom.html', context)


def advisor_events(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')
 
    if not request.user.is_staff or request.user.is_superuser:
        return redirect('/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if request.method == 'POST':
        if request.POST.get('event_title') and request.POST.get('event_des') and request.POST.get('club'):
            has_club = Club.objects.filter(id=request.POST.get('club')).first()
            if has_club:
                e=Event.objects.create(
                    user=request.user,
                    club=has_club,
                    title = request.POST.get('event_title'),
                    description = request.POST.get('event_des'),
                    status = False,
                )
            return redirect('/console/advisor/events/')
    
    if request.method == 'GET' and request.GET.get('delete'):
        has_event = Event.objects.filter(id=request.GET.get('delete')).first()
        if has_event:
            has_event.delete()
            return redirect('/console/advisor/events/')

    clubs = Club.objects.all().order_by('-id')
    events = Event.objects.filter(user=request.user).order_by('-id')
    context = {
        'clubs': clubs,
        'events': events,
    }
    return render(request, 'console/advisor-events.html', context)

def advisor_enquiries(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if not request.user.is_staff or request.user.is_superuser:
        return redirect('/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if request.method == 'POST':
        if request.POST.get('a') and request.POST.get('id'):
            e = Enquiry.objects.filter(id=request.POST.get('id')).first()

            if e:
                e.answer = request.POST.get('a')
                e.replyer = request.user

                e.save()
            return redirect('/console/advisor/student-enquiries/')


    enquiries = Enquiry.objects.all().order_by('-id')

    context = {
        'enquiries': enquiries
    }
    return render(request, 'console/advisor-enquiries.html', context)




# students
def student_console(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if request.user.is_staff or request.user.is_superuser:
        return redirect('/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    context = {

    }
    return render(request, 'console/student.html', context)

def student_club(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if request.user.is_staff or request.user.is_superuser:
        return redirect('/')
    
    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if request.GET.get('join'):
        has_club = Club.objects.filter(id=request.GET.get('join')).first()
        if has_club:
            is_joined = ClubMember.objects.filter(user=request.user, club=has_club).first()
            if not is_joined:
                ClubMember.objects.create(
                    user=request.user,
                    club=has_club
                )
        return redirect('/console/student/club/')

    if request.GET.get('leave'):
        is_joined = ClubMember.objects.filter(id=request.GET.get('leave'),user=request.user).first()
        if is_joined:
            is_joined.delete()
        return redirect('/console/student/club/')
        

    myclubs = ClubMember.objects.filter(user=request.user)

    clubs = Club.objects.all().order_by('-id')

    context = {
        'clubs': clubs,
        'myclubs': myclubs,
    }
    return render(request, 'console/student-club.html', context)

def student_events(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if request.user.is_staff or request.user.is_superuser:
        return redirect('/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    events = Event.objects.filter(status=True).order_by('-id')

    context = {
        'events': events
    }
    return render(request, 'console/student-events.html', context)

def student_enquiries(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if request.user.is_staff or request.user.is_superuser:
        return redirect('/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if request.method == 'POST':
        if request.POST.get('q'):
            Enquiry.objects.create(
                user=request.user,
                question=request.POST.get('q'),
            )
        return redirect('/console/student/enquiries/')
    
    enquiries = Enquiry.objects.filter(user=request.user)

    context = {
        'enquiries': enquiries,
    }
    return render(request, 'console/student-enquiries.html', context)

def student_profile(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    if request.user.is_staff or request.user.is_superuser:
        return redirect('/')

    if not request.user.profile.is_email_verified:
        return redirect('/accounts/verify/')

    context = {

    }
    return render(request, 'console/student-profile.html', context)