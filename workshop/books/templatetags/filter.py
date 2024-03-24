from django import template
from accounts.models import Student

register = template.Library()

@register.filter
def format_time(datetime):
    if datetime == None:
        return '-'
    return datetime.strftime("%Y/%m/%d")

@register.filter
def display_borrower(keeper_id):
    if keeper_id == None:
        return '-'
    return Student.objects.get(id=keeper_id).username