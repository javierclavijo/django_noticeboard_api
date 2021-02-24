from django.contrib import admin

# Register your models here.

from noticeboard.models import Notice

admin.site.register(Notice)