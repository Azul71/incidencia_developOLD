from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Departament

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class DepartamentAdmin(admin.ModelAdmin):
     model = Departament

class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'first_name', 'last_name', 'rol_interno','departament','phone', 'password1', 'password2')}
        ),
    )


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None,{'fields':('username','password')}),
        ('Informacion Personal',{'fields':('first_name','last_name','email')}),
        ('Permisos',{'fields':('is_active','is_staff','is_superuser','groups','user_permissions')}),
        ('Otros', {'fields':('rol_interno','phone','departament')})
    )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id','email', 'username','rol_interno','phone']

admin.site.register(Departament) 
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group) 