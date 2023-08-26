from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm
from accounts.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'phone',
                    'avatar',
                    'bio',
                    'gender',
                )
            }
        )
    )
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'is_staff',
                    'phone',
                    'avatar',
                    'bio',
                    'gender',
                )
            }
        )
    )


admin.site.register(User, CustomUserAdmin)
