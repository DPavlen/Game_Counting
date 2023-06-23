from django.contrib import admin

from players.models import Player, Game, Payment, Team



class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id','main_alias', 'other_aliases', 
                    'telegram_login', 'phone', 'banks')
admin.site.register(Player, PlayerAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ('id','url', 'ledger', 
                    'picture')
admin.site.register(Game, GameAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','game', 'payer', 
                    'recipient', 'value', 'paid', 'received')
admin.site.register(Payment, PaymentAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','players', 'admin')
admin.site.register(Team, TeamAdmin)