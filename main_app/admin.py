from django.contrib import admin
from .models import Activity, Photo, Travel

# Register your models here.

admin.site.register(Travel)
admin.site.register(Activity)
admin.site.register(Photo)