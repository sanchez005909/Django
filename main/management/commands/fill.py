from django.core.management import BaseCommand
from main.models import Category, Product
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        return os.system("python manage.py loaddata data.json")
