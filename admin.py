from django.contrib import admin

from .models import Otp


@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    readonly_fields = ('code',)
    list_display = ('code','token','key',)
