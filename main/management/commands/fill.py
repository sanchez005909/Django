from django.core.management import BaseCommand
import json
from main.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        data_list = load_data_json('data.json')

        # categories_for_create = []
        # products_for_create = []
        for el in data_list:
            if 'name_category' in el['fields']:
                Category.objects.create(**el['fields'])
            elif 'name_product' in el['fields']:
                Product.objects.create(**el['fields'])

        # Category.objects.bulk_create(categories_for_create)
        # Product.objects.bulk_create(products_for_create)


def load_data_json(file):
    with open(file) as f:
        templates = json.load(f)
    return templates
