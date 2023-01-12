from django.contrib import admin
from .models import Work, Goal
# Register your models here.


@admin.register(Work, Goal)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'abstract', 'user', 'deadline', 'created_at']
    search_fields = ['title', 'status', 'abstract']
    list_editable = ['status']
    list_filter = ['deadline', 'created_at']
    raw_id_fields=['user']
