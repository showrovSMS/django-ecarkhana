from django.db import models

# Create your models here.


class Prices(models.Model):

    previous_selling_price = models.DecimalField("previous Selling Price", max_digits=25, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField("Discount", null=True, blank=True, default=0)
    buying_price = models.DecimalField("Buying Price", max_digits=25, decimal_places=2, null=True, blank=True)
    selling_price = models.IntegerField("Selling Price", null=True, blank=True)
    image_url = models.TextField("Image URL", null=True, blank=True)
    timestamp = models.DateTimeField("Timestamp", null=True, blank=True, auto_now_add=True)


    class Meta:
        verbose_name_plural = "Prices"
    def _str_(self):
        return str(self.id)

#customer

class Customers(models.Model):

    customers_id = models.IntegerField(null=True, blank=True)
    company_name = models.TextField(null=True, blank=True)
    contact_name = models.TextField(null=True, blank=True)
    contact_title = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    postal_code = models.TextField(null=True, blank=True)
    region = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    fax = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Customers"
    def _str_(self):
        return str(self.id)


class CustomersCustomersdemo(models.Model):

    customers_id =  models.ForeignKey(Customers, null=True, blank=True, on_delete=models.DO_NOTHING)
    customer_type = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "CustomersCustomersdemo"
    def _str_(self):
        return str(self.id)



class Customersdemographics(models.Model):

    customers_id =  models.ForeignKey(CustomersCustomersdemo, null=True, blank=True, on_delete=models.DO_NOTHING)
    customer_type = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Customersdemographics"
    def _str_(self):
        return str(self.id)



#suppliers

class Suppliers(models.Model):

    suppliers_id = models.IntegerField(null=True, blank=True)
    company_name = models.TextField(null=True, blank=True)
    contact_name = models.TextField(null=True, blank=True)
    contact_title = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    postal_code = models.TextField(null=True, blank=True)
    region = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    fax = models.TextField(null=True, blank=True)
    homepage = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name_plural = "Suppliers"
    def _str_(self):
        return str(self.id)

#shipper

class Shipper(models.Model):

    shipper_id = models.IntegerField(null=True, blank=True)
    company_name = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Shipper"
    def _str_(self):
        return str(self.id)





#orders

class Orders(models.Model):

    order_id = models.IntegerField(null=True, blank=True)
    customer_id = models.ForeignKey(Shipper, null=True, blank=True, on_delete=models.DO_NOTHING)
    employee_id = models.IntegerField(null=True, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    required_date = models.DateTimeField(null=True, blank=True)
    shipped_date = models.DateTimeField(null=True, blank=True)
    shipped_via = models.ForeignKey(Shipper, null=True, blank=True, on_delete=models.DO_NOTHING)
    freight = models.DecimalField(null=True, blank=True, max_digits=25, decimal_places=2)
    ship_name = models.TextField(null=True, blank=True)
    ship_address = models.TextField(null=True, blank=True)
    ship_city = models.TextField(null=True, blank=True)
    ship_region = models.TextField(null=True, blank=True)
    ship_postal_code = models.TextField(null=True, blank=True)
    ship_country = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Orders"
    def _str_(self):
        return str(self.id)



# categories

class Categories(models.Model):
    category_id = models.IntegerField(null=True, blank=True)
    category_name = models.TextField(null=True, blank=True)
    description= models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def _str_(self):
        return str(self.id)



    # product

class Product(models.Model):

    product_id = models.IntegerField(null=True, blank=True)
    supplier_id = models.ForeignKey(Suppliers, null=True, blank=True, on_delete=models.DO_NOTHING)   #Foregeien key
    category_id =  models.ForeignKey(Categories, null=True, blank=True, on_delete=models.DO_NOTHING)   #Foregeien key
    product_name = models.TextField(null=True, blank=True)
    quantity_per_unit = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(null=True, blank=True, max_digits=25, decimal_places=2)
    units_in_stoke = models.IntegerField(null=True, blank=True)
    units_in_order = models.IntegerField(null=True, blank=True)
    reorder_level = models.IntegerField(null=True, blank=True)



    class Meta:
        verbose_name_plural = "Product"
    def _str_(self):
        return str(self.id)





#order details

class Ordersdetails(models.Model):

    order_id =  models.ForeignKey(Orders, null=True, blank=True, on_delete=models.DO_NOTHING)
    product_id =  models.ForeignKey(Product, null=True, blank=True, on_delete=models.DO_NOTHING)
    quantity_id = models.IntegerField(null=True, blank=True)
    unit_price_decimel = models.DecimalField(null=True, blank=True, max_digits=25, decimal_places=2)
    discount_double = models.DecimalField(null=True,  blank=True, max_digits=25, decimal_places=2)

    class Meta:
        verbose_name_plural = "Ordersdetails"
    def _str_(self):
        return str(self.id)
