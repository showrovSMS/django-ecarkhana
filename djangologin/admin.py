from django.contrib import admin

# Register your models here.
from djangologin.models import *

#
# @admin.register(Prices)
# class AdminPrices(admin.ModelAdmin):
#     list_display = [f.name for f in Prices._meta.fields]


#e-carkhana

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = [f.name for f in User._meta.fields]

@admin.register(Guest)
class AdminGuest(admin.ModelAdmin):
    list_display = [f.name for f in Guest._meta.fields]


@admin.register(Roles)
class AdminRoles(admin.ModelAdmin):
    list_display = [f.name for f in Roles._meta.fields]

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = [f.name for f in Product._meta.fields]


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = [f.name for f in Cart._meta.fields]

@admin.register(Cart_item)
class AdminCart_item(admin.ModelAdmin):
    list_display = [f.name for f in Cart_item._meta.fields]


@admin.register(Orders)
class AdminOrders(admin.ModelAdmin):
    list_display = [f.name for f in Orders._meta.fields]

@admin.register(Orders_status)
class AdminOrders_status(admin.ModelAdmin):
    list_display = [f.name for f in Orders_status._meta.fields]


@admin.register(General)
class AdminGeneralr(admin.ModelAdmin):
    list_display = [f.name for f in General._meta.fields]


@admin.register(Product_categori)
class AdminProduct_categori(admin.ModelAdmin):
    list_display = [f.name for f in Product_categori._meta.fields]


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = [f.name for f in Review._meta.fields]


@admin.register(Traffic)
class AdminTraffic(admin.ModelAdmin):
    list_display = [f.name for f in Traffic._meta.fields]


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = [f.name for f in Blog._meta.fields]



@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = [f.name for f in Message._meta.fields]



@admin.register(Reply_message)
class AdminReply_message(admin.ModelAdmin):
    list_display = [f.name for f in Reply_message._meta.fields]



@admin.register(Home_slider)
class AdminHome_slider(admin.ModelAdmin):
    list_display = [f.name for f in Home_slider._meta.fields]









