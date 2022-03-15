from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    # Officer
    path('admin/', admin_console, name='admin_console'),
    path('admin/club/', admin_club, name='admin_club'),
    path('admin/classrooms/', admin_classrooms, name='admin_classrooms'),
    path('admin/events/', admin_events, name='admin_events'),
    path('admin/student-enquiries/', admin_enquiries, name='admin_enquiries'),
    path('admin/manage-users/', admin_manage_users, name='admin_manage_users'),


    # advisor
    path('advisor/',advisor_console, name='advisor_console'),
    path('advisor/classrooms/', advisor_classrooms, name='advisor_classrooms'),
    path('advisor/events/', advisor_events, name='advisor_events'),
    path('advisor/student-enquiries/', advisor_enquiries, name='advisor_enquiries'),


    # Student
    path('student/', student_console, name='student_console'),
    path('student/club/', student_club, name='student_club'),
    path('student/events/', student_events, name='student_events'),
    path('student/enquiries/', student_enquiries, name='student_enquiries'),
    path('student/profile/', student_profile, name='student_profile'),
]
