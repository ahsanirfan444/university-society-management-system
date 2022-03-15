from django import template
from console.models import Club, ClubMember


register = template.Library()

@register.filter
def member_count(value):
    return ClubMember.objects.filter(club__id=value).count()

@register.filter
def already_req(value, arg):
    joined = ClubMember.objects.filter(user=arg, club=value)
    if joined:
        return True
    else:
        return False