from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myauth.models import ClientUser


# Register your models here.
class ClientUserAdmin(UserAdmin):
    pass


admin.site.register(ClientUser, ClientUserAdmin)
