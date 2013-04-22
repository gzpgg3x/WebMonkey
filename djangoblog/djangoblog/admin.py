from django.contrib import admin
from blog.models import Entry
from blog.admin import EntryAdmin
class AdminSite(admin.AdminSite):
    pass
site = AdminSite()
site.register(Entry, EntryAdmin)
