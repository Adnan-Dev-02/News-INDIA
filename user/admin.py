from django.contrib import admin
from .models import *
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display=("Name", "Email", "Mobile", "Message")
admin.site.register(contactus, contactusAdmin)

class igalleryAdmin(admin.ModelAdmin):
    list_display = ("gname", "gpic")
admin.site.register(igallery, igalleryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ("shead", "ssubject", "sdes", "spic")
admin.site.register(slider, sliderAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ("ncity", "cpic", "ndate")
admin.site.register(city, cityAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ("category", "cpic", "cdate")
admin.site.register(ncategory, categoryAdmin)

class mynewsAdmin(admin.ModelAdmin):
    list_display = ("id", "ntitle", "nhead", "ndes", "npic", "ncity", "category", "ndate")
admin.site.register(mynews, mynewsAdmin)

class videonewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'vlink', 'vhead', 'vcategory', 'vcity', 'vdate', 'vdes')
admin.site.register(videonews, videonewsAdmin)