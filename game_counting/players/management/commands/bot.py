from typing import Any, Optional
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args: Any, **options: Any) -> str:
        """Вызов bot в manage.py."""
        pass
        # return super().handle(*args, **options)