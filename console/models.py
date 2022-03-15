from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1024)
    approved = models.BooleanField(default=True)

    at = models.DateField(auto_now_add=True)

class ClubMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    status = models.BooleanField(default=False)

    at = models.DateField(auto_now_add=True)

class Classroom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boot_to', null=True, blank=True)
    name = models.CharField(max_length=40)
    room = models.IntegerField()
    link = models.CharField(max_length=200)

    book_date = models.DateTimeField(blank=True, null=True)

    at = models.DateField(auto_now_add=True)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=2048)

    status = models.BooleanField(default=False)

    at = models.DateField(auto_now_add=True)


class Enquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    replyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replyers', blank=True, null=True)
    question = models.CharField(max_length=120)
    answer = models.TextField(max_length=1024, blank=True, null=True)

    at = models.DateTimeField(auto_now_add=True)


