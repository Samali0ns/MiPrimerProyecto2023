from django.contrib import admin
from .models import Profileuser

@admin.register(Profileuser)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone', 'birth_date')