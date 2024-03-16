from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def time_since(datetime):
    now = timezone.now()
    timedelta = now - datetime
    minutes = int(timedelta.days*24*60 + timedelta.seconds / 60)
    return minutes

@register.filter
def format_time(datetime):
    if datetime == None:
        return '-'
    return datetime.strftime("%Y/%m/%d")

@register.filter
def length(list):
    return len(list)