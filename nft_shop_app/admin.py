from django.contrib import admin

from .models import Nft


class NftAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'productivity']


admin.site.register(Nft, NftAdmin)
