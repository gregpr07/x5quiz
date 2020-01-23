from django import template

from accounts.models import ProfileStatistics

register = template.Library()


@register.filter(name='fetch_points')
def fetch_points(user):
    return ProfileStatistics.objects.get(user=user).points
