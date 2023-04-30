from django.contrib import admin
from inventory import models


admin.site.register(models.Category)
admin.site.register(models.Item)