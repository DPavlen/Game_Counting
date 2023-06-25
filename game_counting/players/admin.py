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
    list_display = ('id','game', 'player', 
                    'recipient', 'value', 'paid', 'received')
admin.site.register(Payment, PaymentAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','display_players', 'display_game')
    def display_players(self, obj):
        """Преобразование для ManyToMany. Основной игрок."""
        return ", ".join([player.main_alias for player in obj.players.all()])
    
    def display_game(self, obj):
        """Преобразование для ManyToMany. URL игры."""
        return ", ".join([game.url for game in obj.game.all()])
admin.site.register(Team, TeamAdmin)



    # def display_admin(self, obj):
    #     return ", ".join([admin.name for admin in obj.admin.all()])
