from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Account)
class AccountAdmin(admin.ModelAdmin):
    search_fields = ('username', )
admin.site.register(Address)
admin.site.register(Shop)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Collect)