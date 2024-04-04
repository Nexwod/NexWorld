from django.contrib import admin

from . models import Estate, Realtor, Branch,Purchase
# Register your models here.

admin.site.register(Estate)
admin.site.register(Realtor)
admin.site.register(Branch)
admin.site.register(Purchase)