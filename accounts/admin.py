from django.contrib import admin

from accounts.models import Profile, ProfileStatistics

admin.site.register(Profile)
admin.site.register(ProfileStatistics)

