from django.contrib import admin
from .models import Account
from .models import AccountTransfer
from .models import Product

# Register your models here.
admin.site.register(Account)
admin.site.register(AccountTransfer)
admin.site.register(Product)