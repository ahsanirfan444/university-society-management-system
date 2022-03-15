from django.urls import path
from .views import *

urlpatterns = [
    path('', accounts),
    path('login/', log_in, name='login'),
    path('change-password/', change, name='change'),
    path('signup/', signup, name='signup'),
    path('verify/', verify, name='verify'),
    path('logout/', log_out, name='logout')
]
