from django.contrib import admin
from .models import Tag, CustomUser


class TagInline(admin.TabularInline):
    model = Tag
    fields =['name']
    extra = 0
@admin.register(Tag)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'level', 'parrent']
    list_filter = ['level']
    search_fields = ['name']
    fields = ['name','parrent']
    inlines = [TagInline]    


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username','email']
    list_filter = ['tags','is_active', 'is_staff', 'is_superuser', 'is_company_admin']

    