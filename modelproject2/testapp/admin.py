from django.contrib import admin
from . import models
# Register your models here.
class hydmodel_admin(admin.ModelAdmin):
    list_display=["id","date","company","title","eligibility","address","email","phonenumber"]

admin.site.register(models.hydjobs,hydmodel_admin)

class punemodel_admin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]

admin.site.register(models.punejobs,punemodel_admin)

class bangmodel_admin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]

admin.site.register(models.bangjobs,bangmodel_admin)