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



# datainsert

def datainsert(request):
    print('this is showing')
    Blog.objects.all().delete()
    Userss.objects.all().delete()
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


    obj = Blog()
    obj.blog_id = 1
    obj.blog_name = 'hello world'
    obj.blog_des = 'hello worldhello worldhello worldhello worldhello worldhello world'
    obj.user_id = Userss.objects.get(user_id=1)
    obj.img_url = 'facebook.com'
    obj.created_at_date = datetime.datetime.now()
    obj.updated_at_date = datetime.datetime.now()
    obj.save()

# data update

    upd = Userss.objects.get(user_id=2)
    upd.user_name = 'nazmul'
    upd.save()


#data delete

    upd = Userss.objects.get(user_id=2)
    upd.delete()
