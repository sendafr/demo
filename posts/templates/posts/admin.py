from django.contrib import admin
from django.db import models

from image_uploader_widget.widgets import ImageUploaderWidget
from.models import My_Profile
# Register your models here.


@admin.register(My_Profile)
class My_ProfileAdmin(admin.ModelAdmin):
    formfield_overrides ={
        models.ImageField:{'widget':ImageUploaderWidget},
    }
   