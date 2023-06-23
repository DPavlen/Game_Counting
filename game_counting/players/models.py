from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Player(models.Model):
    """Модель игрока. Основные атрибуты и функции."""

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

    def add_alias(self):
        """Добавляет alias в строку other_aliases через запятую."""
        pass
    
    def change_alias(self):
        """Изменяет main_alias на новый, если новый был в строке other_aliases,
        то его оттуда удалить, текущий можно записать в other_aliases (не точно)."""
        pass

    def add_phone(self):
        """Добавляет телефон."""
        pass   

    def change_phon(self):
        """Изменение телефона."""
        pass    

    def change_bank(self):
        """Изменение банка."""
        pass  
    
    def change_telegram(self):
        """Изменение telegram."""


class Game(models.Model):
    """Модель игры. Основные атрибуты и функции."""

    id = models.AutoField(verbose_name="идентификатор игры",
                          primary_key=True)
    url = models.CharField(verbose_name="URL игры",
                                  max_length=255)
    ledger = models.CharField(verbose_name="??????",
                                     max_length=255, null=True, blank=True)
    picture = models.ImageField(blank=True)


    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def create_game(self):
        """Создает новую игры по ссылке."""
        pass


class Payment(models.Model):
    """Модель оплаты. Основные атрибуты и функции."""

    id = models.AutoField(verbose_name="идентификатор игры",
                          primary_key=True)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='Игра'
    )
    payer = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='Игрок'
    )
    recipient = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='Players'
    )
    value = models.FloatField(verbose_name="Значение суммы платежа",
                             max_length=30, null=True, blank=True)
    paid = models.BooleanField(verbose_name="Оплачено",
                             max_length=10, null=True, blank=True)
    received = models.BooleanField(verbose_name="Оплата получена",
                             max_length=10, null=True, blank=True)
    

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def add_paymment(self):
        """Добавляет платеж в систему."""
        pass

    def set_payment_paied(self):
        """Выставляет paid=True, оплачено."""
        pass

    def set_payment_received(self):
        """выставляет received=True, оплата получена"""
        pass


class Team(models.Model):
    """Модель оплаты. Основные атрибуты и функции."""

    id = models.AutoField(verbose_name="идентификатор команды",
                          primary_key=True)
    # list[Player] for player??
    players = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='players'
    )
    admin = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='admin'
    )
    
    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def create_team(self):
        """Cоздаёт новую команду."""
        pass

    def add_member(self):
        """Добавляет игрока в команду."""
        pass


# функции class Player: 
	# add_alias: добавляет alias в строку other_aliases через запятую
	# change_alias: изменяет main_alias на новый, если новый был в строке other_aliases, то его оттуда удалить, текущий можно записать в other_aliases (не точно)
	# add_phone: добавить phone
	# change_phone: изменить phone
	# add_bank: добавить bank
	# change_bank: изменить bank
	# change_telegram: изменить telegram



# функции class Game: 
	# create_game: создаёт новую игру по ссылке




# class Payment функции: 
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