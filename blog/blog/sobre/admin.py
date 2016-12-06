from django.contrib import admin

from .models import SobreNos

# Register your models here.

class SobreNosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')

admin.site.register(SobreNos, SobreNosAdmin)
