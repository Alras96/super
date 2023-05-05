from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import CustomUser,AddProduct


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()    
    class Meta:
        model =CustomUser
        fields = ['username','email','password1','password2']
        
        
class AddProductForm(forms.ModelForm):
    class Meta:
        model =AddProduct
        fields = ['barcode_no','brand','product_name','manufacture_date','expiry_date','total_quantity','product_quantity','q_measurements','sale_price','mrp','purchase_amount','tq_units']
        
        
class GeneratecodeForm(forms.ModelForm):
    class Meta:
        model =AddProduct
        fields = ['brand','product_name','manufacture_date','expiry_date','total_quantity','product_quantity','q_measurements','sale_price','mrp','purchase_amount','tq_units']