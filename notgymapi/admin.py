from django.contrib import admin
from .models import Classdetail
from notgymapi import models

admin.site.register(Classdetail)
admin.site.register(models.UserProfile)
