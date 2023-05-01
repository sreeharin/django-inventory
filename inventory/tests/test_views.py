'''
Tests for views
'''
import sys
from django.test import TestCase, Client
from django.urls import reverse
from inventory.models import Category, Item


def create_category(name='sample category'):
    '''Create and return category'''
    return Category.objects.create(name=name)

def create_item(category=None, **item_details):
    '''Create and return item'''
    if not category:
        category = create_category()
    sample_details = {
        'name': 'test item',
        'quantity': 1,
        'description': 'test description.'
    }
    sample_details.update(item_details)
    return Item.objects.create(category=category, **sample_details)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_category_list_view(self):
        '''Test for views.CategoryListView'''
        URL = reverse('inventory:index')
        create_category()
        create_category()
        res = self.client.get(URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context['object_list']), 2)

    def test_category_items_view(self):
        '''Test for views.CategoryItemsListView'''
        item = create_item()
        URL = reverse('inventory:category-items', args=[item.category.pk])
        res = self.client.get(URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context['object_list']), 1)

    def test_item_search_view(self):
        '''Test for views.ItemSearchView'''
        item = create_item()
        create_item(category=item.category, name='new thing')
        URL = reverse('inventory:search')
        res = self.client.get(URL, {'query': item.name})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context['object_list']), 1)