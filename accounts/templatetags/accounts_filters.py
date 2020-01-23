from django import template

from accounts.models import ProfileStatistics

register = template.Library()


@register.filter(name='fetch_karma')
def fetch_karma(user):
    return ProfileStatistics.objects.get(user=user).karma
