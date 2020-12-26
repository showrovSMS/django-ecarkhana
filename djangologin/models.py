from django.db import models

# Create your models here.

#
# class Prices(models.Model):
#
#     previous_selling_price = models.DecimalField("previous Selling Price", max_digits=25, decimal_places=2, null=True, blank=True)
#     discount = models.IntegerField("Discount", null=True, blank=True, default=0)
#     buying_price = models.DecimalField("Buying Price", max_digits=25, decimal_places=2, null=True, blank=True)
#     selling_price = models.IntegerField("Selling Price", null=True, blank=True)
#     image_url = models.TextField("Image URL", null=True, blank=True)
#     timestamp = models.DateTimeField("Timestamp", null=True, blank=True, auto_now_add=True)
#
#
#     class Meta:
#         verbose_name_plural = "Prices"
#     def _str_(self):
#         return str(self.id)

#user

class User(models.Model):

    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.TextField(null=True, blank=True)
    user_email = models.EmailField(null=True, blank=True)
    current_password = models.TextField(null=True, blank=True)
    new_password = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    registrated_at_date = models.TextField(null=True, blank=True)
    login_at_date = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "User"
    def _str_(self):
        return str(self.id)


#guest

class Guest(models.Model):

    guest_id = models.IntegerField(null=True, blank=True)
    guest_name = models.TextField(null=True, blank=True)
    guest_email = models.EmailField(null=True, blank=True)
    current_password = models.TextField(null=True, blank=True)
    new_password = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    image_url = models.ImageField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    registrated_at_date = models.TextField(null=True, blank=True)
    login_at_date = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Guest"
    def _str_(self):
        return str(self.id)




#roles

class Roles(models.Model):

    roles_id = models.IntegerField(null=True, blank=True)
    user_id =  models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    name = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    permission = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Roles"
    def _str_(self):
        return str(self.id)



#traffic

class Traffic(models.Model):

    traffic_id = models.IntegerField(null=True, blank=True)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    ip = models.IntegerField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=25, decimal_places=2, null=True, blank=True)
    longitude = models.DecimalField(max_digits=25, decimal_places=2, null=True, blank=True)
    browser = models.TextField(null=True, blank=True)
    browser_version = models.DecimalField(max_digits=25, decimal_places=2, null=True, blank=True)
    platform = models.TextField(null=True, blank=True)
    device = models.TextField(null=True, blank=True)
    visited_page = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Traffic"
    def _str_(self):
        return str(self.id)






# product

class Product(models.Model):

    product_id = models.IntegerField(null=True, blank=True)
    sku = models.TextField(null=True, blank=True)
    product_name = models.TextField(null=True, blank=True)
    product_des = models.TextField(null=True, blank=True)
    img_url = models.TextField(null=True, blank=True)
    product_price = models.TextField(null=True, blank=True)
    product_type = models.TextField(null=True, blank=True)
    product_category = models.TextField(null=True, blank=True)
    product_cart_details = models.TextField(null=True, blank=True)
    product_available = models.TextField(null=True, blank=True)
    product_stock = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)
    deleted_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Product"
    def _str_(self):
        return str(self.id)



#product_review+comment

class Review(models.Model):

    review_id = models.IntegerField(null=True, blank=True)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    comments_box = models.TextField(null=True, blank=True)
    review_box = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name_plural = "Review"


    def _str_(self):
        return str(self.id)



# product_categories

class Product_categori(models.Model):

    cat_id = models.IntegerField(null=True, blank=True)
    cate_name = models.TextField(null=True, blank=True)
    cate_slug = models.TextField(null=True, blank=True)
    img_url = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)
    deleted_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Product_categori"
    def _str_(self):
        return str(self.id)


#general_specification


class General(models.Model):

    general_id = models.IntegerField(null=True, blank=True)
    bike_type = models.TextField(null=True, blank=True)
    brand = models.TextField(null=True, blank=True)
    model = models.TextField(null=True, blank=True)
    displacement = models.TextField(null=True, blank=True)
    regis_year = models.IntegerField(null=True, blank=True)
    kms_driven = models.IntegerField(null=True, blank=True)
    no_of_gear = models.IntegerField(null=True, blank=True)
    weight = models.TextField(null=True, blank=True)
    made_of_origin = models.TextField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    condition = models.TextField(null=True, blank=True)
    engine_type = models.TextField(null=True, blank=True)
    max_power = models.TextField(null=True, blank=True)
    ground_clereance = models.TextField(null=True, blank=True)
    suspension = models.TextField(null=True, blank=True)
    fueL_tank_capacity = models.TextField(null=True, blank=True)
    brake_system = models.TextField(null=True, blank=True)
    kerb_weight = models.TextField(null=True, blank=True)
    top_speed = models.TextField(null=True, blank=True)
    bore = models.TextField(null=True, blank=True)
    stroke = models.TextField(null=True, blank=True)
    max_torque = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "General"
    def _str_(self):
        return str(self.id)



#cart

class Cart(models.Model):

    cart_id = models.IntegerField(null=True, blank=True)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)
    deleted_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Cart"
    def _str_(self):
        return str(self.id)

#cart_item

class Cart_item(models.Model):

    cart_item_id = models.IntegerField(null=True, blank=True)
    product_id = models.ForeignKey(Product, null=True, blank=True, on_delete=models.DO_NOTHING)
    cart_id = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.DO_NOTHING)
    sku = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    discount = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)
    deleted_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Cart_item"
    def _str_(self):
        return str(self.id)

#orders_status

class Orders_status(models.Model):

    order_status_id = models.IntegerField(null=True, blank=True)
    pending_payment = models.TextField(null=True, blank=True)
    failed = models.TextField(null=True, blank=True)
    processing = models.TextField(null=True, blank=True)
    completed = models.TextField(null=True, blank=True)
    on_hold = models.TextField(null=True, blank=True)
    cancelled = models.TextField(null=True, blank=True)
    refunded = models.TextField(null=True, blank=True)
    authentication_required = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Orders_status"
    def _str_(self):
        return str(self.id)


#orders

class Orders(models.Model):

    order_id = models.IntegerField(null=True, blank=True)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    cart_id = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.DO_NOTHING)
    session_id = models.IntegerField(null=True, blank=True)
    order_status_id = models.ForeignKey(Orders_status, null=True, blank=True, on_delete=models.DO_NOTHING)
    order_status = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)
    deleted_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Orders"
    def _str_(self):
        return str(self.id)


# categories

class Categories(models.Model):
    category_id = models.IntegerField(null=True, blank=True)
    category_name = models.TextField(null=True, blank=True)
    description= models.TextField(null=True, blank=True)
    img_url = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def _str_(self):
        return str(self.id)



# blog

class Blog(models.Model):
    blog_id = models.IntegerField(null=True, blank=True)
    blog_name = models.TextField(null=True, blank=True)
    blog_des = models.TextField(null=True, blank=True)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    img_url = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Blog"

    def _str_(self):
        return str(self.id)



# Home_slider

class Home_slider(models.Model):
    slider_id = models.IntegerField(null=True, blank=True)
    device = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img_url = models.TextField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Home_slider"

    def _str_(self):
        return str(self.id)


# message_box

class Message(models.Model):
    mess_id = models.IntegerField(null=True, blank=True)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    text_box = models.TextField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Message"

    def _str_(self):
        return str(self.id)




# Reply_message_box

class Reply_message(models.Model):
    reply_id = models.IntegerField(null=True, blank=True)
    message_id = models.ForeignKey(Message, null=True, blank=True, on_delete=models.DO_NOTHING)
    text_box = models.TextField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    created_at_date = models.TextField(null=True, blank=True)
    updated_at_date = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Reply_message"

    def _str_(self):
        return str(self.id)







