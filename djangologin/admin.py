from django.contrib import admin

# Register your models here.
from djangologin.models import *


@admin.register(Prices)
class AdminPrices(admin.ModelAdmin):
    list_display = [f.name for f in Prices._meta.fields]


@admin.register(Suppliers)
class AdminSuppliers(admin.ModelAdmin):
    list_display = [f.name for f in Suppliers._meta.fields]


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = [f.name for f in Product._meta.fields]

@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    list_display = [f.name for f in Categories._meta.fields]


@admin.register(Customers)
class AdminCustomers(admin.ModelAdmin):
    list_display = [f.name for f in Customers._meta.fields]

@admin.register(CustomersCustomersdemo)
class AdminCustomersCustomersdemo(admin.ModelAdmin):
    list_display = [f.name for f in CustomersCustomersdemo._meta.fields]

@admin.register(Customersdemographics)
class AdminCustomersdemographics(admin.ModelAdmin):
    list_display = [f.name for f in Customersdemographics._meta.fields]

@admin.register(Orders)
class AdminOrders(admin.ModelAdmin):
    list_display = [f.name for f in Orders._meta.fields]

@admin.register(Ordersdetails)
class AdminOrdersdetails(admin.ModelAdmin):
    list_display = [f.name for f in Ordersdetails._meta.fields]

@admin.register(Shipper)
class AdminShipper(admin.ModelAdmin):
    list_display = [f.name for f in Shipper._meta.fields]









