from django.contrib import admin
from users.models import UserProfile, UserTraining, UserWeight

admin.site.register(UserProfile)
admin.site.register(UserTraining)
admin.site.register(UserWeight)
