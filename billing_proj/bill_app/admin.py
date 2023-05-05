from django.contrib import admin
from .models import CustomUser,AddProduct,SalesInvoice,SalesProduct,GenerateProduct

admin.site.register(CustomUser)
admin.site.register(AddProduct)
admin.site.register(SalesInvoice)
admin.site.register(SalesProduct)
admin.site.register(GenerateProduct)