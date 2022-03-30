from django.contrib import admin


from .models import Menu, Mahsulot


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ['nomi']
    list_display = ['nomi']
    
    


@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    search_fields = ['nomi','menu','mahsulot_haqida','narx']
    list_display = ['nomi','menu','mahsulot_haqida','narx']