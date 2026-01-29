from django.contrib import admin
from .models import Hotel, CustomUser
from django.contrib.auth.admin import UserAdmin

# Pour le CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

# Pour le Hotel
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'owner', 'created_at')
    search_fields = ('name',)
