from django.db import models
from django.contrib.auth.models import AbstractUser

# barcode generater
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


ROLE_CHOICES=(
    
    ('Admin', 'Admin'),
    ('User', 'User'),

)

PAYMENT_CHOICES=(
    
    ('Cash', 'Cash'),
    ('Card', 'Card'),
    ('UPI', 'UPI'),

)

MEASUREMENT_CHOICES=(
    
    ('ml', 'ml'),
    ('L', 'L'),
    ('g', 'g'),
    ('Kg', 'Kg'),
    ('Pcs', 'Pcs'),

)

UNIT_CHOICES=(
    
    ('Litre', 'Litre'),
    ('Kg', 'Kg'),
    ('Pcs', 'Pcs'),

)

class CustomUser(AbstractUser):
    
    is_role=models.CharField(max_length=255, choices=ROLE_CHOICES,null=True)
    email=models.EmailField(('email address'),unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    username = models.CharField(max_length=255,null=True)
    custom_password=models.CharField(max_length=255,null=True)
    custom_worker=models.BooleanField(default=False,null=True)
    
    active=models.BooleanField(default=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

class GenerateProduct(models.Model):
    barcode_no=models.CharField(max_length=12, null=True)
    barcode = models.ImageField(upload_to='images/', blank=True)
    product_name=models.CharField(max_length=255, null=True)
    bar_img_no=models.CharField(max_length=255, null=True,blank=True)
    

    def __str__(self):
        return str(self.product_name)

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.barcode_no}', writer=ImageWriter())
        print('one rejin da')
        print(ean)
        self.bar_img_no=ean
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.product_name}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)    


class AddProduct(models.Model):
    
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    generate_product=models.ForeignKey(GenerateProduct,on_delete=models.CASCADE,null=True,blank=True)
    barcode_no=models.CharField(max_length=255, null=True,unique=True)
    brand=models.CharField(max_length=255, null=True,blank=True)
    product_name=models.CharField(max_length=255, null=True)
    manufacture_date=models.DateTimeField(null=True,blank=True)
    expiry_date=models.DateTimeField(null=True,blank=True)
    total_quantity=models.DecimalField(max_digits=300, decimal_places=2,null=True) 
    stock_quantity=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True)
    product_quantity=models.DecimalField(max_digits=300, decimal_places=2,null=True) 
    sale_price=models.DecimalField(max_digits=300, decimal_places=2,null=True)  # per piece or kg or litre
    mrp=models.DecimalField(max_digits=300, decimal_places=2,null=True,blank=True)
    purchase_amount=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)
    cal_amount=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)  #  quantity * sale_price
    active=models.BooleanField(default=True,null=True)
    status=models.BooleanField(default=True,null=True)
    expiry=models.BooleanField(default=False,null=True)
    generate=models.BooleanField(default=False,null=True)
    q_measurements=models.CharField(max_length=255, choices=MEASUREMENT_CHOICES,null=True)
    tq_units=models.CharField(max_length=255, choices=UNIT_CHOICES,null=True)
    out_of_stock=models.BooleanField(default=False,null=True)
    sold_quantity=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)
    sold=models.BooleanField(default=False,null=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    
       
class SalesInvoice(models.Model):
    
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    sales_bill_no= models.CharField(max_length=200, null=True,blank=True)
    grand_total=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)       # Round of value
    amount_received=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)
    balance_return=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)
    payment_type=models.CharField(max_length=255, choices=PAYMENT_CHOICES,null=True,blank=True)
    total_items=models.CharField(max_length=200, null=True,blank=True)
    savings=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


class SalesProduct(models.Model):
    
    invoice=models.ForeignKey(SalesInvoice,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(AddProduct,on_delete=models.CASCADE,null=True,blank=True)
    sale_quantity=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)
    price=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)
    total_amount= models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)
    mrp=models.DecimalField(default=0.00,max_digits=300, decimal_places=2,null=True,blank=True)
    enter_product=models.CharField(max_length=255,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
