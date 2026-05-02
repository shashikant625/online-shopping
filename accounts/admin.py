from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,UserProfile
from django.utils.html import format_html

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name", "last_login", "date_joined", "is_active")

    list_filter = ("is_admin", "is_active")  
    
    list_display_links = ("email","first_name","last_name")

    filter_horizontal = ()  

    fieldsets = ()   # ✅ fieldsates → fieldsets

    readonly_fields = ("last_login", "date_joined")   # ✅ important fix



from django.contrib import admin
from django.utils.html import format_html
from .models import UserProfile, Account


class UserProfileAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        if object.profile_picture:   
            return format_html(
                '<img src="{}" width="30" style="border-radius:50%;">',
                object.profile_picture.url  
            )
        return 

    thumbnail.short_description = 'Profile Picture'

    list_display = ('thumbnail', 'user', 'city', 'state', 'country')


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)