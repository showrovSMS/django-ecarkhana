from django.db.models import Q
from django.shortcuts import render
from djangologin.models import *
import datetime
# Create your views here.
def abc(request):

    return render(request,"front end/index.html",{'question_object':"",'option_objects': ""})

def abc2(request):

    return render(request,"front end/bike-index.html",{'question_object':"",'option_objects': ""})

def abc3(request):

    return render(request,"front end/bicycle-index.html",{'question_object':"",'option_objects': ""})

def abc4(request):

    return render(request,"front end/auction-bidding-list.html",{'question_object':"",'option_objects': ""})

def abc5(request):

    return render(request,"front end/auction-product-list.html",{'question_object':"",'option_objects': ""})

def abc6(request):

    return render(request,"front end/bicycle-compare.html",{'question_object':"",'option_objects': ""})

def abc7(request):

    return render(request,"front end/bike-cart.html",{'question_object':"",'option_objects': ""})
def abc8(request):

    return render(request,"front end/bike-checkout.html",{'question_object':"",'option_objects': ""})

def abc9(request):

    return render(request,"front end/bike-compare.html",{'question_object':"",'option_objects': ""})

def abc10(request):

    return render(request,"front end/bike-fit-calculator.html",{'question_object':"",'option_objects': ""})

def abc11(request):

    return render(request,"front end/bike-listing.html",{'question_object':"",'option_objects': ""})

def abc12(request):

    return render(request,"front end/bike-wishlist.html",{'question_object':"",'option_objects': ""})

def abc13(request):

    return render(request,"front end/car-ad-post.html",{'question_object':"",'option_objects': ""})

def abc14(request):

    return render(request,"front end/car-insurance.html",{'question_object':"",'option_objects': ""})

def abc15(request):

    return render(request,"front end/car-listing.html",{'question_object':"",'option_objects': ""})

def abc16(request):

    return render(request,"front end/car-loan.html",{'question_object':"",'option_objects': ""})

def abc17(request):

    return render(request,"front end/car-loan-eligibility.html",{'question_object':"",'option_objects': ""})


def abc18(request):

    return render(request,"front end/car-loan-insurance-check.html",{'question_object':"",'option_objects': ""})


def abc19(request):

    return render(request,"front end/compare-car.html",{'question_object':"",'option_objects': ""})

def abc20(request):

    return render(request,"front end/contact us.html",{'question_object':"",'option_objects': ""})

def abc21(request):

    return render(request,"front end/dealer-details.html",{'question_object':"",'option_objects': ""})

def abc22(request):

    return render(request,"front end/dealer-list.html",{'question_object':"",'option_objects': ""})

def abc23(request):

    return render(request,"front end/group-buying-list.html",{'question_object':"",'option_objects': ""})

def abc24(request):

    return render(request,"front end/national-distributor-details.html",{'question_object':"",'option_objects': ""})

def abc25(request):

    return render(request,"front end/national-distributor-list.html",{'question_object':"",'option_objects': ""})

def abc26(request):

    return render(request,"front end/Privacy-Policy.html",{'question_object':"",'option_objects': ""})

def abc27(request):

    return render(request,"front end/search-page.html",{'question_object':"",'option_objects': ""})

def abc28(request):

    return render(request,"front end/sell-product-list.html",{'question_object':"",'option_objects': ""})

def abc29(request):

    return render(request,"front end/seller-message.html",{'question_object':"",'option_objects': ""})

def abc30(request):

    return render(request,"front end/seller-my-ad.html",{'question_object':"",'option_objects': ""})

def abc31(request):

    return render(request,"front end/seller-profile.html",{'question_object':"",'option_objects': ""})

def abc32(request):

    return render(request,"front end/single-accessories.html",{'question_object':"",'option_objects': ""})

def abc33(request):

    return render(request,"front end/single-bike-product.html",{'question_object':"",'option_objects': ""})

def abc34(request):

    return render(request,"front end/single-blog.html",{'question_object':"",'option_objects': ""})

def abc35(request):

    return render(request,"front end/single-car-product.html",{'question_object':"",'option_objects': ""})

def abc36(request):

    return render(request,"front end/single-sell-product.html",{'question_object':"",'option_objects': ""})

def abc37(request):

    return render(request,"front end/Terms And Conditions.html",{'question_object':"",'option_objects': ""})


# def queryLearn(request):

    # blog_list = Blog.objects.all()
    # print("hello owrld", len(blog_list))
    # for obj in blog_list:
    #     print(obj.blog_name)
    #
    # user_list = Userss.objects.all()
    # for kaj in user_list:
    #     print(kaj.user_name,"  ", kaj.user_email)
    #
    # # find_user = Userss.objects.get(user_id = 4)
    # # print(find_user.user_id)
    #
    # find_blog = Blog.objects.get(blog_name='hello world')
    # print(find_blog.blog_id)
    #
    #
    # find_blog = Blog.objects.filter(blog_name='hello world')
    # for sms in find_blog:
    #     print(sms.blog_id)
    #
    # find_usersss = Userss.objects.filter(user_name='showrov', user_id=1)
    # for shv in find_usersss:
    #     print(shv.user_name)

# User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))

    # find_usersss = Userss.objects.filter(Q(user_name='showrov') | Q(user_id=1))
    # for shv in find_usersss:
    #     print(shv.user_name)
    #
    # find_blog = Blog.objects.filter(user_id__user_name='showrov')
    # for sms in find_blog:
    #     print(sms.blog_name)
    #
    #
    # return render(request, "front end/Terms And Conditions.html", {'question_object': "", 'option_objects': ""})


# datainsert

def datainsert(request):
    print('this is showing')
    # Blog.objects.all().delete()
    # Userss.objects.all().delete()
    usr = Userss()
    usr.user_id = 1
    usr.user_name = 'showrov'
    usr.user_email = 'showrov.storerepublic@gmail.com'
    usr.current_password = 'showrov.storerepublic'
    usr.new_password = 'showrov.storerepublic'
    usr.country = 'Bangladesh'
    usr.image_url = 'facebook.com'
    usr.phone = '01745227509'
    usr.address = 'Mohammadpur'
    usr.billing_address = 'Mohammadpur'
    usr.shipping_address = 'Mohammadpur'
    usr.registrated_at_date = '12 jun'
    usr.login_at_date = datetime.datetime.now()
    usr.created_at_date = datetime.datetime.now()
    usr.save()

    usr = Userss()
    usr.user_id = 2
    usr.user_name = 'shakir'
    usr.user_email = 'showrov@gmail.com'
    usr.current_password = 'showrov.storerepublic'
    usr.new_password = 'showrov.storerepublic'
    usr.country = 'India'
    usr.image_url = 'facebook.com'
    usr.phone = '01710607515'
    usr.address = 'Dhanmondhi'
    usr.billing_address = 'Mohammadpur'
    usr.shipping_address = 'Mohammadpur'
    usr.registrated_at_date = '12 jun'
    usr.login_at_date = datetime.datetime.now()
    usr.created_at_date = datetime.datetime.now()
    usr.save()

    usr = Userss()
    usr.user_id = 3
    usr.user_name = 'sms'
    usr.user_email = 'showrov26692@gmail.com'
    usr.current_password = 'showrov.storerepublic'
    usr.new_password = 'showrov.storerepublic'
    usr.country = 'Japan'
    usr.image_url = 'facebook.com'
    usr.phone = '01721762968'
    usr.address = 'azimpur'
    usr.billing_address = 'Mohammadpur'
    usr.shipping_address = 'Mohammadpur'
    usr.registrated_at_date = '12 jun'
    usr.login_at_date = datetime.datetime.now()
    usr.created_at_date = datetime.datetime.now()
    usr.save()

    usr = Userss()
    usr.user_id = 4
    usr.user_name = 'Kamrul'
    usr.user_email = 'kamrul@gmail.com'
    usr.current_password = 'showrov.storerepublic'
    usr.new_password = 'showrov.storerepublic'
    usr.country = 'Malaysia'
    usr.image_url = 'facebook.com'
    usr.phone = '01738200964'
    usr.address = 'new market'
    usr.billing_address = 'Mohammadpur'
    usr.shipping_address = 'Mohammadpur'
    usr.registrated_at_date = '12 jun'
    usr.login_at_date = datetime.datetime.now()
    usr.created_at_date = datetime.datetime.now()
    usr.save()

    usr = Userss()
    usr.user_id = 5
    usr.user_name = 'mahid'
    usr.user_email = 'mahid@gmail.com'
    usr.current_password = 'showrov.storerepublic'
    usr.new_password = 'showrov.storerepublic'
    usr.country = 'Malaysia'
    usr.image_url = 'facebook.com'
    usr.phone = '017104563456'
    usr.address = 'new market'
    usr.billing_address = 'Mohammadpur'
    usr.shipping_address = 'Mohammadpur'
    usr.registrated_at_date = '12 jun'
    usr.login_at_date = datetime.datetime.now()
    usr.created_at_date = datetime.datetime.now()
    usr.save()

    return render(request, "front end/Terms And Conditions.html", {'question_object': "", 'option_objects': ""})


def bloginsert(request):
    print('hello this is blog')
    obj = Blog()
    obj.blog_id = 1
    obj.blog_name = 'hello world'
    obj.blog_des = 'hello worldhello worldhello worldhello worldhello worldhello world'
    obj.user_id = Userss.objects.get(user_id=2)
    obj.img_url = 'facebook.com'
    obj.created_at_date = datetime.datetime.now()
    obj.updated_at_date = datetime.datetime.now()
    obj.save()

    obj = Blog()
    obj.blog_id = 2
    obj.blog_name = 'hello world-2'
    obj.blog_des = 'hello worldhello worldhello worldhello worldhello worldhello world'
    obj.user_id = Userss.objects.get(phone = '01738200964')
    obj.img_url = 'facebook.com'
    obj.created_at_date = datetime.datetime.now()
    obj.updated_at_date = datetime.datetime.now()
    obj.save()

    obj = Blog()
    obj.blog_id = 3
    obj.blog_name = 'hello world-3'
    obj.blog_des = 'hello worldhello worldhello worldhello worldhello worldhello world'
    obj.user_id = Userss.objects.get(address = 'Mohammadpur')
    obj.img_url = 'facebook.com'
    obj.created_at_date = datetime.datetime.now()
    obj.updated_at_date = datetime.datetime.now()
    obj.save()

    obj = Blog()
    obj.blog_id = 4
    obj.blog_name = 'hello world-4'
    obj.blog_des = 'hello worldhello worldhello worldhello worldhello worldhello world'
    obj.user_id = Userss.objects.get(country = 'India')
    obj.img_url = 'facebook.com'
    obj.created_at_date = datetime.datetime.now()
    obj.updated_at_date = datetime.datetime.now()
    obj.save()

    obj = Blog()
    obj.blog_id = 5
    obj.blog_name = 'hello world-5'
    obj.blog_des = 'hello worldhello worldhello worldhello worldhello worldhello world'
    obj.user_id = Userss.objects.get(user_email = 'showrov26692@gmail.com')
    obj.img_url = 'facebook.com'
    obj.created_at_date = datetime.datetime.now()
    obj.updated_at_date = datetime.datetime.now()
    obj.save()

    return render(request,"front end/single-blog.html",{'question_object':"",'option_objects': ""})

def prtinsert(request):
    print('this is for product')
    prd = Product()
    prd.product_id = 1
    prd.sku = 'aper34542f'
    prd.product_name = 'Demo'
    prd.product_des = 'lorem2jnklvndfvndlkfvndkfvn,dnb,dfmnpiodfhb,nmcmxv,xuiertj9dfjfdknvm,g dfndf vjpdfoibdb n0'
    prd.img_url = 'https://88aura.com'
    prd.product_price = '350 taka'
    prd.product_type = 'new'
    prd.product_category = 'bike'
    prd.product_cart_details = 'two new bike'
    prd.product_available = '200 piece'
    prd.product_stock = '4000 piece'
    prd.created_at_date = datetime.datetime.now()
    prd.updated_at_date = datetime.datetime.now()
    prd.deleted_at_date = datetime.datetime.now()
    prd.save()

    prd = Product()
    prd.product_id = 2
    prd.sku = 'aperdfg42f'
    prd.product_name = 'title'
    prd.product_des = 'lorem2jnklvndfvndlkfvndkfvn,dnb,dfmnpiodfhb,nmcmxv,xuiertj9dfjfdknvm,g dfndf vjpdfoibdb n0'
    prd.img_url = 'https://activelpg.com'
    prd.product_price = '5650 taka'
    prd.product_type = 'used'
    prd.product_category = 'cycle'
    prd.product_cart_details = 'one new bicycle'
    prd.product_available = '260 piece'
    prd.product_stock = '4700 piece'
    prd.created_at_date = datetime.datetime.now()
    prd.updated_at_date = datetime.datetime.now()
    prd.deleted_at_date = datetime.datetime.now()
    prd.save()

    prd = Product()
    prd.product_id = 3
    prd.sku = 'sms34542f'
    prd.product_name = 'Shakir'
    prd.product_des = 'lorem2jnklvndfvndlkfvndkfvn,dnb,dfmnpiodfhb,nmcmxv,xuiertj9dfjfdknvm,g dfndf vjpdfoibdb n0'
    prd.img_url = 'https://timeless.com'
    prd.product_price = '4540 taka'
    prd.product_type = 'recondition'
    prd.product_category = 'bike'
    prd.product_cart_details = 'four new bike'
    prd.product_available = '30 piece'
    prd.product_stock = '450 piece'
    prd.created_at_date = datetime.datetime.now()
    prd.updated_at_date = datetime.datetime.now()
    prd.deleted_at_date = datetime.datetime.now()
    prd.save()

    prd = Product()
    prd.product_id = 4
    prd.sku = 'aperfd452f'
    prd.product_name = 'druto'
    prd.product_des = 'lorem2jnklvndfvndlkfvndkfvn,dnb,dfmnpiodfhb,nmcmxv,xuiertj9dfjfdknvm,g dfndf vjpdfoibdb n0'
    prd.img_url = 'https://druto.com'
    prd.product_price = '35440 taka'
    prd.product_type = 'new'
    prd.product_category = 'bike'
    prd.product_cart_details = 'two new bike'
    prd.product_available = '2100 piece'
    prd.product_stock = '40300 piece'
    prd.created_at_date = datetime.datetime.now()
    prd.updated_at_date = datetime.datetime.now()
    prd.deleted_at_date = datetime.datetime.now()
    prd.save()

    return render(request, "front end/single-bike-product.html", {'question_object': "", 'option_objects': ""})

def crtinsert(request):
    print("this is for cart")
    crt = Cart()
    crt.cart_id = 1
    crt.user_id = Userss.objects.get(user_id=5)
    crt.created_at_date = datetime.datetime.now()
    crt.updated_at_date = datetime.datetime.now()
    crt.deleted_at_date = datetime.datetime.now()
    crt.save()

    crt = Cart()
    crt.cart_id = 2
    crt.user_id = Userss.objects.get(user_id=4)
    crt.created_at_date = datetime.datetime.now()
    crt.updated_at_date = datetime.datetime.now()
    crt.deleted_at_date = datetime.datetime.now()
    crt.save()

    crt = Cart()
    crt.cart_id = 3
    crt.user_id = Userss.objects.get(user_id=1)
    crt.created_at_date = datetime.datetime.now()
    crt.updated_at_date = datetime.datetime.now()
    crt.deleted_at_date = datetime.datetime.now()
    crt.save()

    crt = Cart()
    crt.cart_id = 4
    crt.user_id = Userss.objects.get(user_id=3)
    crt.created_at_date = datetime.datetime.now()
    crt.updated_at_date = datetime.datetime.now()
    crt.deleted_at_date = datetime.datetime.now()
    crt.save()

    crt = Cart()
    crt.cart_id = 5
    crt.user_id = Userss.objects.get(user_id=2)
    crt.created_at_date = datetime.datetime.now()
    crt.updated_at_date = datetime.datetime.now()
    crt.deleted_at_date = datetime.datetime.now()
    crt.save()

    return render(request, "front end/bike-cart.html", {'question_object': "", 'option_objects': ""})

def crtIteminsert(request):
    crtItem =Cart_item()
    crtItem.cart_item_id = 1
    crtItem.cart_id = Cart.objects.get(cart_id=2)
    crtItem.sku = '234fdhjru5'
    crtItem.price = '4550 taka'
    crtItem.discount = '48 taka'
    crtItem.quantity = 400
    crtItem.created_at_date = datetime.datetime.now()
    crtItem.updated_at_date = datetime.datetime.now()
    crtItem.deleted_at_date = datetime.datetime.now()
    crtItem.save()

    crtItem =Cart_item()
    crtItem.cart_item_id = 2
    crtItem.cart_id = Cart.objects.get(cart_id=5)
    crtItem.sku = '234fdft54ru5'
    crtItem.price = '53450 taka'
    crtItem.discount = '348 taka'
    crtItem.quantity = 100
    crtItem.created_at_date = datetime.datetime.now()
    crtItem.updated_at_date = datetime.datetime.now()
    crtItem.deleted_at_date = datetime.datetime.now()
    crtItem.save()


    crtItem =Cart_item()
    crtItem.cart_item_id = 3
    crtItem.cart_id = Cart.objects.get(cart_id=3)
    crtItem.sku = '234fdft54ru5'
    crtItem.price = '2450 taka'
    crtItem.discount = '3348 taka'
    crtItem.quantity = 140
    crtItem.created_at_date = datetime.datetime.now()
    crtItem.updated_at_date = datetime.datetime.now()
    crtItem.deleted_at_date = datetime.datetime.now()
    crtItem.save()

    return render(request, "front end/bike-fit-calculator.html", {'question_object': "", 'option_objects': ""})


def geninsert(request):
    gen = General()
    gen.general_id = 1
    gen.bike_type ='new'
    gen.brand = 'Suzuki'
    gen.model = 'gixxer sf fi'
    gen.displacement = 'test'
    gen.regis_year = 2020
    gen.kms_driven = 145
    gen.no_of_gear = 5
    gen.weight = '147kg'
    gen.made_of_origin = 'japan'
    gen.color = 'black'
    gen.condition = 'new'
    gen.engine_type = '4 stroke'
    gen.max_power = '155cc'
    gen.ground_clereance = 'yes'
    gen.suspension = 'mono stock'
    gen.fueL_tank_capacity= '12.5 litre'
    gen.brake_system= 'both disk brake'
    gen.kerb_weight= '149 kg'
    gen.top_speed='150 km/h'
    gen.bore = 'true'
    gen.stroke= '4 th'
    gen.max_torque= '12.5 cc'
    gen.created_at_date = datetime.datetime.now()
    gen.updated_at_date = datetime.datetime.now()
    gen.save()

    gen = General()
    gen.general_id = 2
    gen.bike_type = 'new'
    gen.brand = 'bajaj'
    gen.model = 'discover'
    gen.displacement = 'testBajaj'
    gen.regis_year = 2021
    gen.kms_driven = 140
    gen.no_of_gear = 4
    gen.weight = '137kg'
    gen.made_of_origin = 'India'
    gen.color = 'red'
    gen.condition = 'new'
    gen.engine_type = '4 stroke'
    gen.max_power = '150cc'
    gen.ground_clereance = 'yes'
    gen.suspension = 'double stock'
    gen.fueL_tank_capacity = '11.5 litre'
    gen.brake_system = 'single disk brake'
    gen.kerb_weight = '143 kg'
    gen.top_speed = '130 km/h'
    gen.bore = 'true'
    gen.stroke = '4 th'
    gen.max_torque = '11.5 cc'
    gen.created_at_date = datetime.datetime.now()
    gen.updated_at_date = datetime.datetime.now()
    gen.save()

    gen = General()
    gen.general_id = 3
    gen.bike_type = 'used'
    gen.brand = 'R 15'
    gen.model = 'indonesian'
    gen.displacement = 'indotest'
    gen.regis_year = 2019
    gen.kms_driven = 155
    gen.no_of_gear = 6
    gen.weight = '157kg'
    gen.made_of_origin = 'Indonesia'
    gen.color = 'Matte black'
    gen.condition = 'new'
    gen.engine_type = '4 stroke'
    gen.max_power = '165cc'
    gen.ground_clereance = 'yes'
    gen.suspension = 'mono stock'
    gen.fueL_tank_capacity = '13.5 litre'
    gen.brake_system = 'both disk brake'
    gen.kerb_weight = '153 kg'
    gen.top_speed = '150 km/h'
    gen.bore = 'true'
    gen.stroke = '4 th'
    gen.max_torque = '14.5 cc'
    gen.created_at_date = datetime.datetime.now()
    gen.updated_at_date = datetime.datetime.now()
    gen.save()

    return render(request, "front end/bike-index.html", {'question_object': "", 'option_objects': ""})

def gstinsert(request):
    gst = Guest()
    gst.guest_id = 1
    gst.guest_name = 'hridoy'
    gst.guest_email = 'hridoy@gmail.com'
    gst.current_password = 'asdf123456'
    gst.new_password = 'asdf123456'
    gst.country = 'Bangladesh'
    gst.image_url = 'www.facebook.com/hridoy'
    gst.phone = '01677543822'
    gst.address = 'barisal'
    gst.billing_address = 'sadar, barisal'
    gst.shipping_address = 'sadar barisal'
    gst.registrated_at_date = datetime.datetime.now()
    gst.login_at_date = datetime.datetime.now()
    gst.created_at_date = datetime.datetime.now()
    gst.save()


    gst = Guest()
    gst.guest_id = 2
    gst.guest_name = 'Oli'
    gst.guest_email = 'oli@gmail.com'
    gst.current_password = 'Weasdf123456'
    gst.new_password = 'Weasdf123456'
    gst.country = 'India'
    gst.image_url = 'www.facebook.com/oli'
    gst.phone = '01733255437'
    gst.address = 'khulna'
    gst.billing_address = 'sadar, khulna'
    gst.shipping_address = 'sadar satkhira'
    gst.registrated_at_date = datetime.datetime.now()
    gst.login_at_date = datetime.datetime.now()
    gst.created_at_date = datetime.datetime.now()
    gst.save()

    gst = Guest()
    gst.guest_id = 3
    gst.guest_name = 'Amirul'
    gst.guest_email = 'amirul@gmail.com'
    gst.current_password = 'Amiasdf123456'
    gst.new_password = 'Amiasdf123456'
    gst.country = 'japan'
    gst.image_url = 'www.facebook.com/amirul'
    gst.phone = '0168072534'
    gst.address = 'chenwan'
    gst.billing_address = 'sajja'
    gst.shipping_address = 'sajja'
    gst.registrated_at_date = datetime.datetime.now()
    gst.login_at_date = datetime.datetime.now()
    gst.created_at_date = datetime.datetime.now()
    gst.save()

    return render(request, "front end/bicycle-index.html", {'question_object': "", 'option_objects': ""})

def hmsinsert(request):
    hms = Home_slider()
    hms.slider_id = 1
    hms.device = 'Asus'
    hms.title = 'home 1'
    hms.description = 'lorem30'
    hms.img_url = 'https://activelpgbd.com/timeless/'
    hms.created_at_date = datetime.datetime.now()
    hms.updated_at_date = datetime.datetime.now()
    hms.save()

    hms = Home_slider()
    hms.slider_id = 2
    hms.device = 'Xiomi'
    hms.title = 'home 2'
    hms.description = 'welorem40'
    hms.img_url = 'https://activelpgbd.com'
    hms.created_at_date = datetime.datetime.now()
    hms.updated_at_date = datetime.datetime.now()
    hms.save()

    hms = Home_slider()
    hms.slider_id = 3
    hms.device = 'Samsung'
    hms.title = 'home 3'
    hms.description = 'Samsungwelorem40'
    hms.img_url = 'https://88aura.com'
    hms.created_at_date = datetime.datetime.now()
    hms.updated_at_date = datetime.datetime.now()
    hms.save()

    return render(request, "front end/auction-bidding-list.html", {'question_object': "", 'option_objects': ""})


def smsinsert(request):
    sms = Message()
    sms.mess_id = 1
    sms.user_id = Userss.objects.get(user_id = 2)
    sms.text_box = 'jbfdsbfnvbkvbnbaslfkjlwrepihjbmb knvfg;jojbhy'
    sms.time = datetime.datetime.now()
    sms.created_at_date = datetime.datetime.now()
    sms.updated_at_date = datetime.datetime.now()
    sms.save()

    sms = Message()
    sms.mess_id = 2
    sms.user_id = Userss.objects.get(user_id = 4)
    sms.text_box = 'jbfdsbfnvbkvbnbaslfkjlwrepihgfrfdghfgr bgsaua sua jbmb knvfg;jojbhy'
    sms.time = datetime.datetime.now()
    sms.created_at_date = datetime.datetime.now()
    sms.updated_at_date = datetime.datetime.now()
    sms.save()

    sms = Message()
    sms.mess_id = 3
    sms.user_id = Userss.objects.get(user_id = 2)
    sms.text_box = 'jbfdsbfnvbkvbnbasasadwerwdgffhudn9plfb hvrhyclfkjlwrepihjbmb knvfg;jojbhy'
    sms.time = datetime.datetime.now()
    sms.created_at_date = datetime.datetime.now()
    sms.updated_at_date = datetime.datetime.now()
    sms.save()

    return render(request, "front end/auction-product-list.html", {'question_object': "", 'option_objects': ""})


def ordinsert(request):
    ordst = Orders_status()
    ordst.order_status_id = 1
    ordst.pending_payment = 'pending'
    ordst.failed = 'failed'
    ordst.processing = 'processing'
    ordst.completed = 'completed'
    ordst.on_hold = 'hold'
    ordst.cancelled = 'cancelled'
    ordst.refunded = 'refunded'
    ordst.authentication_required = 'two step'
    ordst.save()

    ordst = Orders_status()
    ordst.order_status_id = 2
    ordst.pending_payment = 'pending'
    ordst.failed = 'failed'
    ordst.processing = 'processing'
    ordst.completed = 'completed'
    ordst.on_hold = 'hold'
    ordst.cancelled = 'cancelled'
    ordst.refunded = 'refunded'
    ordst.authentication_required = 'two step'
    ordst.save()

    ordst = Orders_status()
    ordst.order_status_id = 3
    ordst.pending_payment = 'pending'
    ordst.failed = 'failed'
    ordst.processing = 'processing'
    ordst.completed = 'completed'
    ordst.on_hold = 'hold'
    ordst.cancelled = 'cancelled'
    ordst.refunded = 'refunded'
    ordst.authentication_required = 'two step'
    ordst.save()

    ordst = Orders_status()
    ordst.order_status_id = 4
    ordst.pending_payment = 'pending'
    ordst.failed = 'failed'
    ordst.processing = 'processing'
    ordst.completed = 'completed'
    ordst.on_hold = 'hold'
    ordst.cancelled = 'cancelled'
    ordst.refunded = 'refunded'
    ordst.authentication_required = 'two step'
    ordst.save()

    ordst = Orders_status()
    ordst.order_status_id = 5
    ordst.pending_payment = 'pending'
    ordst.failed = 'failed'
    ordst.processing = 'processing'
    ordst.completed = 'completed'
    ordst.on_hold = 'hold'
    ordst.cancelled = 'cancelled'
    ordst.refunded = 'refunded'
    ordst.authentication_required = 'two step'
    ordst.save()

    # Order

    ord = Orders()
    ord.order_id = 1
    ord.user_id = Userss.objects.get(user_id = 1)
    ord.cart_id = Cart.objects.get(cart_id = 2)
    ord.session_id = 12
    ord.order_status_id = Orders_status.objects.get(order_status_id = 2)
    ord.order_status = 'pending'
    ord.created_at_date = datetime.datetime.now()
    ord.updated_at_date = datetime.datetime.now()
    ord.deleted_at_date = datetime.datetime.now()
    ord.save()


    ord = Orders()
    ord.order_id = 2
    ord.user_id = Userss.objects.get(user_id = 4)
    ord.cart_id = Cart.objects.get(cart_id = 3)
    ord.session_id = 2
    ord.order_status_id = Orders_status.objects.get(order_status_id = 1)
    ord.order_status = 'completed'
    ord.created_at_date = datetime.datetime.now()
    ord.updated_at_date = datetime.datetime.now()
    ord.deleted_at_date = datetime.datetime.now()
    ord.save()

    ord = Orders()
    ord.order_id = 3
    ord.user_id = Userss.objects.get(user_id = 3)
    ord.cart_id = Cart.objects.get(cart_id = 2)
    ord.session_id = 7
    ord.order_status_id = Orders_status.objects.get(order_status_id = 3)
    ord.order_status = 'processing'
    ord.created_at_date = datetime.datetime.now()
    ord.updated_at_date = datetime.datetime.now()
    ord.deleted_at_date = datetime.datetime.now()
    ord.save()

    return render(request, "front end/bicycle-compare.html", {'question_object': "", 'option_objects': ""})


def procinsert(request):
    proc = Product_categori()
    proc.cat_id = 1
    proc.cate_name = 'new'
    proc.cate_slug = 'asdf'
    proc.img_url = 'https://activelpgbd.com/timeless/'
    proc.created_at_date = datetime.datetime.now()
    proc.updated_at_date = datetime.datetime.now()
    proc.deleted_at_date = datetime.datetime.now()
    proc.save()


    proc = Product_categori()
    proc.cat_id = 2
    proc.cate_name = 'used'
    proc.cate_slug = 'qwer'
    proc.img_url = 'https://activelpgbd.com/jovi/'
    proc.created_at_date = datetime.datetime.now()
    proc.updated_at_date = datetime.datetime.now()
    proc.deleted_at_date = datetime.datetime.now()
    proc.save()


    proc = Product_categori()
    proc.cat_id = 3
    proc.cate_name = 'recondition'
    proc.cate_slug = 'zxcv'
    proc.img_url = 'https://activelpgbd.com'
    proc.created_at_date = datetime.datetime.now()
    proc.updated_at_date = datetime.datetime.now()
    proc.deleted_at_date = datetime.datetime.now()
    proc.save()

    proc = Product_categori()
    proc.cat_id = 4
    proc.cate_name = 'new'
    proc.cate_slug = 'asdfgbf'
    proc.img_url = 'https://activelpgbd.com/wp-admin/'
    proc.created_at_date = datetime.datetime.now()
    proc.updated_at_date = datetime.datetime.now()
    proc.deleted_at_date = datetime.datetime.now()
    proc.save()

    return render(request, "front end/bike-checkout.html", {'question_object': "", 'option_objects': ""})


def repinsert(request):
    rep = Reply_message()
    rep.reply_id = 1
    rep.message_id = Message.objects.get(mess_id = 2)
    rep.text_box = 'mnvojbmdvbjkdvbm,dfgvbvbahgpabjvbjvbuibv ljkhgljkn;llj bklnkljgj;l'
    rep.time = datetime.datetime.now()
    rep.created_at_date = datetime.datetime.now()
    rep.updated_at_date = datetime.datetime.now()
    rep.save()

    rep = Reply_message()
    rep.reply_id = 2
    rep.message_id = Message.objects.get(mess_id = 3)
    rep.text_box = 'mnvojbmdvbjkdvbm,dfgvbvuibv ljkhgljkn;llj bklnkljgj;l'
    rep.time = datetime.datetime.now()
    rep.created_at_date = datetime.datetime.now()
    rep.updated_at_date = datetime.datetime.now()
    rep.save()

    rep = Reply_message()
    rep.reply_id = 3
    rep.message_id = Message.objects.get(mess_id = 1)
    rep.text_box = 'mnvojbgljkn;llj bklnkljgj;l'
    rep.time = datetime.datetime.now()
    rep.created_at_date = datetime.datetime.now()
    rep.updated_at_date = datetime.datetime.now()
    rep.save()

    return render(request, "front end/bike-compare.html", {'question_object': "", 'option_objects': ""})


def revadd(request):
    rev = Review()
    rev.review_id = 1
    rev.user_id = Userss.objects.get(user_id = 3)
    rev.comments_box = 'jhfiohfihfklsdfhsodifhskldfhsdoifhd'
    rev.review_box = 'ihhjhoiuhlhihiohiohiohiehfjkfauifbgjmixcomxmhidwxqi zouihfwef,fh h,wfqq'
    rev.created_at_date = datetime.datetime.now()
    rev.updated_at_date = datetime.datetime.now()
    rev.save()

    rev = Review()
    rev.review_id = 2
    rev.user_id = Userss.objects.get(user_id=1)
    rev.comments_box = 'jhfiohfihfklsdfhhskldfhsdoifhd'
    rev.review_box = 'ihhjhoiuhlhihiohcomxmhidwxqi zouihfwef,fh h,wfqq'
    rev.created_at_date = datetime.datetime.now()
    rev.updated_at_date = datetime.datetime.now()
    rev.save()

    rev = Review()
    rev.review_id = 3
    rev.user_id = Userss.objects.get(user_id=2)
    rev.comments_box = 'jhfiohfihfkkldfhsdoifhd'
    rev.review_box = 'ihhjhoiuhlhihiohiogjmixcomxmhidwxqi zouihfwef,fh h,wfqq'
    rev.created_at_date = datetime.datetime.now()
    rev.updated_at_date = datetime.datetime.now()
    rev.save()

    rev = Review()
    rev.review_id = 4
    rev.user_id = Userss.objects.get(user_id=5)
    rev.comments_box = 'jhfiohfihffhskldfhsdoifhd'
    rev.review_box = 'ihhjhoiuhlhihiohiohiohiehfjkfdwxqi zouihfwef,fh h,wfqq'
    rev.created_at_date = datetime.datetime.now()
    rev.updated_at_date = datetime.datetime.now()
    rev.save()

    return render(request, "front end/bike-wishlist.html", {'question_object': "", 'option_objects': ""})


def roladd(request):
    rol = Roles()
    rol.roles_id = 1
    rol.user_id = Userss.objects.get(user_id =5)
    rol.name = 'administrator'
    rol.type = 'admin'
    rol.permission = 'all access'
    rol.created_at_date = datetime.datetime.now()
    rol.updated_at_date = datetime.datetime.now()
    rol.save()

    rol = Roles()
    rol.roles_id = 2
    rol.user_id = Userss.objects.get(user_id =3)
    rol.name = 'user'
    rol.type = 'subscriber'
    rol.permission = 'customer panel'
    rol.created_at_date = datetime.datetime.now()
    rol.updated_at_date = datetime.datetime.now()
    rol.save()

    rol = Roles()
    rol.roles_id = 3
    rol.user_id = Userss.objects.get(user_id =5)
    rol.name = 'editor'
    rol.type = 'edit'
    rol.permission = 'only post'
    rol.created_at_date = datetime.datetime.now()
    rol.updated_at_date = datetime.datetime.now()
    rol.save()

    return render(request, "front end/car-ad-post.html", {'question_object': "", 'option_objects': ""})


def trajoin(request):
    tra = Traffic()
    tra.traffic_id = 1
    tra.user_id = Userss.objects.get(user_id = 5)
    tra.ip = 120
    tra.latitude ='103.24565'
    tra.longitude ='-9845.25'
    tra.browser = 'opera'
    tra.browser_version = '3.35'
    tra.platform = 'coding'
    tra.device = 'desktop'
    tra.visited_page = 'desinghjfklf'
    tra.created_at_date = datetime.datetime.now()
    tra.updated_at_date = datetime.datetime.now()
    tra.save()

    tra = Traffic()
    tra.traffic_id = 2
    tra.user_id = Userss.objects.get(user_id=4)
    tra.ip = 128
    tra.latitude = '103.65'
    tra.longitude = '-985.25'
    tra.browser = 'safari'
    tra.browser_version = '3.35'
    tra.platform = 'coding'
    tra.device = 'phone'
    tra.visited_page = 'fgffrc'
    tra.created_at_date = datetime.datetime.now()
    tra.updated_at_date = datetime.datetime.now()
    tra.save()


    tra = Traffic()
    tra.traffic_id = 3
    tra.user_id = Userss.objects.get(user_id=1)
    tra.ip = 127
    tra.latitude = '103.65'
    tra.longitude = '-985.25'
    tra.browser = 'chrome'
    tra.browser_version = '3.35'
    tra.platform = 'coding'
    tra.device = 'laptop'
    tra.visited_page = 'fgdfdfdgffrc'
    tra.created_at_date = datetime.datetime.now()
    tra.updated_at_date = datetime.datetime.now()
    tra.save()

    return render(request, "front end/sell-product-list.html", {'question_object': "", 'option_objects': ""})


























    # prd = Product()
    # prd.product_id = 1
    # prd.sku = 'aper34542f'
    # prd.product_name = 'Demo'
    # prd.product_des = 'lorem2jnklvndfvndlkfvndkfvn,dnb,dfmnpiodfhb,nmcmxv,xuiertj9dfjfdknvm,g dfndf vjpdfoibdb n0'
    # prd.img_url = 'https://88aura.com'
    # prd.product_price = '350 taka'
    # prd.product_type = 'new'
    # prd.product_category = 'bike'
    # prd.product_cart_details = 'two new bike'
    # prd.product_available = '200 piece'
    # prd.product_stock = '4000 piece'
    # prd.created_at_date = datetime.datetime.now()
    # prd.updated_at_date = datetime.datetime.now()
    # prd.deleted_at_date = datetime.datetime.now()
    # prd.save()









# data update
#
#     upd = Userss.objects.get(user_id=1)
#     upd.user_name = 'nazmul'
#     upd.save()


# data delete
#
#     upd = Userss.objects.get(user_id=1)
#     upd.delete()


