from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("email", "is_active", "is_staff", "last_login", "date_joined")
    list_filter = ("is_active", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()
