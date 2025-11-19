# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# admin.site.site_header = "Blog Login"
# admin.site.site_title = "Blog Admin"
# admin.site.index_title = "Welcome to Blog Dashboard"

# class CustomUserAdmin(BaseUserAdmin):
#     def has_module_permission(self, request):
#         return request.user.is_superuser

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
import logging

logger = logging.getLogger(__name__)
logger.debug('blogs.admin module loaded')

class CustomUserAdmin(BaseUserAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
