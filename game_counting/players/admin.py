from django.contrib import admin

from players.models import Player



class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id','main_alias', 'other_aliases', 
                    'telegram_login', 'phone', 'banks')

admin.site.register(Player, PlayerAdmin)