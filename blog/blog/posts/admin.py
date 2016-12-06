from django.contrib import admin

from .models import Post, Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'obs')

class PostAdmin(admin.ModelAdmin):
    exclude = ('autor',)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)
