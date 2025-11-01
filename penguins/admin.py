from django.contrib import admin
from unfold.admin import ModelAdmin

from penguins.models import Penguin

@admin.register(Penguin)
class PenguinsAdmin(ModelAdmin):
    list_display= ["name", "age"]
