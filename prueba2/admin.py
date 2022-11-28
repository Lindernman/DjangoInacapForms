from django.contrib import admin


from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Producto._meta.get_fields()]


admin.site.register(Producto, ProductoAdmin)
