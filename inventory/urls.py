'''
For mapping views with urls
'''
from django.urls import path
from inventory import views


app_name = 'inventory'
urlpatterns = [
    path('', view=views.CategoryListView.as_view(), name='index'),
    path(
        'category/create/', view=views.CategoryCreateView.as_view(),
        name='create-category'),
    path('category/<int:pk>/', view=views.CategoryItemsListView.as_view(),
        name='category-items'),
    path('category/<int:pk>/delete/', view=views.CategoryDeleteView.as_view(),
        name='category-delete'),
    path('category/<int:pk>/create-item/', view=views.ItemCreateView.as_view(),
        name='create-item'),
    path('category/<int:cat_id>/item/<int:pk>/delete/',
        view=views.ItemDeleteView.as_view(), name='item-delete'),
    path('category/<int:cat_id>/item/<int:pk>/edit/',
        view=views.ItemEditView.as_view(), name='item-edit'),
]