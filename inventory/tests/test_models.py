'''
Tests for models
'''
from django.test import TestCase
from inventory.models import Category, Item


def create_item(category: Category, **kwargs: dict[str, any]) -> Item:
    '''Create and return item object'''
    item_details = {
        'name': 'Sample Item',
        'quantity': 1,
        'description': 'Sample Item Description',
    }
    item_details.update(kwargs)
    return Item.objects.create(category=category, **item_details)

class ModelTests(TestCase):
    def test_items_in_category(self):
        '''Test to check if item exists in category'''
        category = Category.objects.create(name='Sample Category')
        item_1 = create_item(category)
        item_2_details = {
            'name': 'Sample Item 2',
        }
        item_2 = create_item(category, **item_2_details)

        self.assertEqual(category.items.count(), 2)
        self.assertEqual(category.items.get(id=1).name, item_1.name)
        self.assertEqual(category.items.get(id=2).name, item_2.name)