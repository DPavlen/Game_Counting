from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Player(models.Model):
    """Модель игрока и его основные атрибуты."""

    id = models.AutoField(verbose_name="идентификатор игрока",
                          primary_key=True)
    main_alias = models.CharField(verbose_name="Основное имя игрока",
                                  max_length=255)
    other_aliases = models.CharField(verbose_name="Другие имена игрока",
                                     max_length=255, null=True, blank=True)
    telegram_login = models.CharField(verbose_name="Логин Telegram",
                                      max_length=100, null=True, blank=True)
    phone = models.CharField(verbose_name="Номер телефона игрока",
                             max_length=20, null=True, blank=True)
    banks = models.CharField(verbose_name="Номер карты или счета",
                             max_length=255, null=True, blank=True)

    def __str__(self):
        return self.main_alias

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"


from django.db import models

# Create your models here.

# class Player
# id: int, primary key
# main_alias: str
# other_aliases: str
# telegram_login: str
# phone: str
# banks: str
# функции: 
	# add_alias: добавляет alias в строку other_aliases через запятую
	# change_alias: изменяет main_alias на новый, если новый был в строке other_aliases, то его оттуда удалить, текущий можно записать в other_aliases (не точно)
	# add_phone: добавить phone
	# change_phone: изменить phone
	# add_bank: добавить bank
	# change_bank: изменить bank
	# change_telegram: изменить telegram



# class Game
# id: int, primary key
# url: str
# ledger: str
# picture: image
# функции: 
	# create_game: создаёт новую игру по ссылке




# class Payment
# id: int, primary key
# game: Game
# payer: Player
# recipient: Player
# value: float
# paid: bool
# received: bool
# функции: 
	# add_paymment: добавляет платеж в систему
	# set_payment_paied: выставляет paid=True
	# set_payment_received: выставляет received=True


# class Team
# id: int, primary key
# players: list[Player]
# admin: Player
# функции: 
	# create_team: создаёт новую команду
	# add_member: добавляет участника в команду