from django.contrib import admin

from cookies.models import Cookie

class CookieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cookie)
