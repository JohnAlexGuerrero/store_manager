from django.contrib import admin

from remission.models import Detail

from remission.forms import DetailForm

# Register your models here.

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    form = DetailForm
