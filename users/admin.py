from django.contrib import admin
from users.models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user', 'phone_number', 'website', 'picture') # Para que se vean estos atributos en la web
    list_display_links = ('pk', 'user') # Para que Estos atributos sean links que llevan al perfil
    list_editable = ('phone_number', 'website', 'picture') # Hace los atributos editables sin entrar en el perfil
    search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name', 'phone_number') # phone number sin user porque no es heredada como las otras
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')