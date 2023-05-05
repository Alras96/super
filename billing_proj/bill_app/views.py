from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser,AddProduct,GenerateProduct,SalesInvoice,SalesProduct
from .forms import UserRegisterForm,AddProductForm,GeneratecodeForm
import datetime
import calendar
from django.http import HttpResponse
from django.http import JsonResponse
import json
# for checking
from django.views.decorators.csrf import csrf_exempt

import random


def error_404_view(request, exception):
    return render(request, 'bill_app/404.html')


# def rand_no():
#     return (random.randint(100000000000,999999999999))

# def randam_no():
#     return ("%0.12d" % random.randint(0,999999999999))

def my_numb():
    return ("%0.12d" % random.randint(0,999999999999))


def bill_no():
    l=SalesInvoice.objects.last()
    if l:
        l=l.id   
    else:
        l=0      
    l=l+1

    return ("BNO" '%01d' % l)


# def product_number():
#     l=GenerateProduct.objects.last()
#     if l:
#         l=l.id   
#     else:
#         l=0      
#     l=l+1

#     return ("" '%01d' % l)

@login_required(login_url='') 
def admin_register(request):
    form=UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)         
        if form.is_valid():
            user=form.save() 
            print(user)
            user.is_role='Admin'
            user.save()
            messages.success(request,'Registered successfully')
            return redirect('admin_register')
        else: 
            messages.warning(request, "Please fill required fields")          
            return render(request,'bill_app/admin_signup.html',context={"form":form})
    else:                                 
        return render(request,'bill_app/admin_signup.html',context={"form":form})

@login_required(login_url='') 
def user_register(request):
    form=UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)         
        if form.is_valid():
            password=request.POST.get('password1')
            print(password)
            user=form.save() 
            print(user)
            user.is_role='User'
            user.custom_password=password
            user.custom_worker=True
            user.save()
            messages.success(request,'Registered successfully')
            return redirect('user_register')
        else: 
            messages.warning(request, "Please fill required fields")          
            return render(request,'bill_app/user_signup.html',context={"form":form})
    else:                                 
        return render(request,'bill_app/user_signup.html',context={"form":form})
    
def login_view(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            email = request.POST.get('email')
            print(email)
            password = request.POST.get('password')
            print(password)
            user = authenticate(username=email,password=password)
            if user: 
                if user.active:
                    if user.is_role=='Admin':
                        login(request, user)
                        
                        take_today=datetime.datetime.now()
                        print(take_today)
                        print(type(take_today)) 
                        
                        products_list=AddProduct.objects.filter(active=True)
                        print(products_list)
                        if products_list:
                            print('yes we have serviced customers')
                            for product in products_list:
                                my_expiry=product.expiry_date
                                if my_expiry != None:
                                    check_expiry_date=product.expiry_date
                                    print(check_expiry_date)
                                    if take_today > check_expiry_date:
                                        print('today date greater than expiry date')
                                        product.expiry=True
                                        product.save()
                                    elif take_today < check_expiry_date:
                                        print('today date smaller than expiry date')
                                    elif take_today == check_expiry_date:
                                        print('today date equal expiry date')
                                        product.expiry=True
                                        product.save()
                                    
                            messages.success(request,f"Hello, {user.username}")
                            # return redirect('home')
                            return redirect('view_stock')
                        else:
                            messages.success(request,f"Hello, {user.username}")
                            # return redirect('home')
                            return redirect('view_stock')
                    
                    elif user.is_staff:
                        login(request, user)
                        
                        take_today=datetime.datetime.now()
                        print(take_today)
                        print(type(take_today))
                        
                        products_list=AddProduct.objects.filter(active=True)
                        print(products_list)
                        if products_list:
                            print('yes we have serviced customers')
                            for product in products_list:
                                my_expiry=product.expiry_date
                                if my_expiry != None:
                                    check_expiry_date=product.expiry_date
                                    print(check_expiry_date)
                                    if take_today > check_expiry_date:
                                        print('today date greater than expiry date')
                                        product.expiry=True
                                        product.save()
                                    elif take_today < check_expiry_date:
                                        print('today date smaller than expiry date')
                                    elif take_today == check_expiry_date:
                                        print('today date equal expiry date')
                                        product.expiry=True
                                        product.save()
                                    
                            messages.success(request,f"Hello, {user.username}")
                            # return redirect('home')
                            return redirect('view_stock')
                            
                        
                        else:
                            messages.success(request,f"Hello, {user.username}")
                            # return redirect('home')
                            return redirect('view_stock')
                            
                    
                    elif user.is_role=='User':
                        login(request, user)
                        
                        take_today=datetime.datetime.now()
                        print(take_today)
                        print(type(take_today))
                        
                        products_list=AddProduct.objects.filter(active=True)
                        print(products_list)
                        if products_list:
                            for product in products_list:
                                my_expiry=product.expiry_date
                                if my_expiry != None:
                                    print('this is not met with condition')
                                    check_expiry_date=product.expiry_date
                                    print(check_expiry_date)
                                    if take_today > check_expiry_date:
                                        print('today date greater than expiry date')
                                        product.expiry=True
                                        product.save()
                                    elif take_today < check_expiry_date:
                                        print('today date smaller than expiry date')
                                    elif take_today == check_expiry_date:
                                        print('today date equal expiry date')
                                        product.expiry=True
                                        product.save()
                                    
                            messages.success(request,f"Hello, {user.username}")
                            return redirect('bill_page')
                        
                        else:
                            messages.success(request,f"Hello, {user.username}")
                            return redirect('bill_page')
                    else:
                        messages.warning(request,"Invalid username or password")
                        return redirect("login")
                else:
                    messages.warning(request,"Contact admin")
                    return redirect("login")
            else:
                messages.warning(request,"Invalid username or password")
                return redirect("login")
        else:
            messages.warning(request,"Please fill the form before submit")
            return redirect("login")
        
    else:
        return render(request, 'bill_app/login.html')
        

@login_required(login_url='') 
def user_logout(request):
    logout(request)  
    messages.success(request, f'You have been logged out successfully')
    return redirect('login') 

@login_required(login_url='')
def update_password(request):
    if request.method== 'POST':
        print('valid aguthu')
        if request.POST.get("password1"):
            print('yes password iruku')
            id=request.POST.get('user_id')
            my_password=request.POST.get("password1")
            print(my_password)
            print(id)
            test=len(my_password)
            print(test)

            user_obj= CustomUser.objects.get(id=id)
            print(user_obj)
            user_obj.set_password(my_password)
            user_obj.custom_password=my_password
            user_obj.save()
            messages.success(request,'Password Updated successfully')
            print('success')
            return redirect('view_users')
        else:
            print('my bad')
            messages.info(request,'Please fill fields correctly')
            return redirect('view_users')
    else:
        return redirect('view_users')
    
    
@login_required(login_url='')
def change_password(request):
    if request.method== 'POST':
        print('valid aguthu')
        if request.POST.get("password1"):
            print('yes password iruku')
            id=request.POST.get('user_id')
            my_password=request.POST.get("password1")
            print(my_password)
            print(id)
            test=len(my_password)
            print(test)

            user_obj= CustomUser.objects.get(id=id)
            print(user_obj)
            user_obj.set_password(my_password)
            user_obj.custom_password=my_password
            user_obj.save()
            messages.success(request,'Password Updated successfully')
            print('success')
            return redirect('login')
        else:
            print('my bad')
            messages.info(request,'Please fill fields correctly')
            return redirect('login')
    else:
        return redirect('login')


@login_required(login_url='') 
def home_view(request):
    return render(request,'bill_app/index.html')
    
@login_required(login_url='') 
def view_users(request):
    users=CustomUser.objects.filter(is_role='User')
    return render(request,'bill_app/users.html',context={'users':users})
   
@login_required(login_url='')
def disable_view(request):
    if request.method =='POST':
        id=request.POST.get('id')
        my_object=CustomUser.objects.get(id=id)
        my_object.active=False
        my_object.save()
        messages.success(request,'User disabled successfully')
        return redirect('view_users')
    else:
        return redirect('view_users')
        

@login_required(login_url='')
def enable_view(request):
    if request.method =='POST':
        id=request.POST.get('id')
        my_object=CustomUser.objects.get(id=id)
        my_object.active=True
        my_object.save()
        messages.success(request,'User Enabled successfully')
        return redirect('view_users')
    else:
        return redirect('view_users')
    
@login_required(login_url='')
def stock_entry(request):
    form=AddProductForm()
    if request.method == 'POST':
        user=request.user
        form=AddProductForm(request.POST)
        if form.is_valid:
            print('form valid boy')
            barcode_no=request.POST.get('barcode_no')
            product_name=request.POST.get('product_name')
            p_brand=request.POST.get('brand')
            tq_units=request.POST.get('tq_units')
            p_unit=request.POST.get('q_measurements')
            
            if request.POST.get('manufacture_date') == '':
                manuf_date=None
            else:
                get_manuf_date=request.POST.get('manufacture_date')
                manuf_date=datetime.datetime.strptime(get_manuf_date, "%Y-%m-%d")
            
            if request.POST.get('expiry_date') == '':
                expiry=None
            else:
                get_expiry=request.POST.get('expiry_date')
                expiry=datetime.datetime.strptime(get_expiry, "%Y-%m-%d")
                e=expiry.date()
                print(e)
            
                today_date=datetime.datetime.now()
                to=today_date.date()
                print(to)
                
                if today_date == expiry:
                    print('the 2 dates are equal')
                    messages.warning(request,'Entered expiry date is today date')
                    return redirect('stock_entry')
                elif today_date > expiry:
                    print('given date less tha today date')
                    messages.warning(request,'Entered expiry date expired')
                    return redirect('stock_entry')
                      
            if request.POST.get('total_quantity') == '':
                total_qty=float(0)
            else:
                try:
                    total_qty=float(request.POST.get('total_quantity'))
                except:
                    total_qty=float(0)
                    
            if request.POST.get('product_quantity') == '':
                product_qty=float(0)
            else:
                try:
                    product_qty=float(request.POST.get('product_quantity'))
                except:
                    product_qty=float(0)
            
            if request.POST.get('sale_price') == '':
                s_price=float(0)
            else:
                try:        
                    s_price=float(request.POST.get('sale_price'))
                except:
                    s_price=float(0)
            
            if request.POST.get('mrp') =='': 
                mrp=float(0)
            else:
                try:       
                    mrp=float(request.POST.get('mrp'))
                except:
                    mrp=float(0)
            
            if request.POST.get('purchase_amount') =='':
                purchase_amt=float(0)
            else:
                try:
                    purchase_amt=float(request.POST.get('purchase_amount'))
                except:
                    purchase_amt=float(0)
                    
            try:
                product=AddProduct.objects.create(barcode_no=barcode_no,brand=p_brand,product_name=product_name,
                                            manufacture_date=manuf_date,expiry_date=expiry,total_quantity=total_qty,
                                            product_quantity=product_qty,tq_units=tq_units,
                                            q_measurements=p_unit,sale_price=s_price,mrp=mrp,purchase_amount=purchase_amt)
            
                
            
            
                # product=form .save()
                q=product.total_quantity
                p=product.sale_price
                product.cal_amount=float(q)*float(p)
                product.user=user
                product.stock_quantity=q
                product.save()
                messages.success(request,'Product added successfully')
                return redirect('stock_entry')
            except:
                messages.info(request,'Entered Barcode already exist')
                return redirect('stock_entry')
                
        else:
            messages.error(request,'Invalid form entiry')
            return render(request,'bill_app/stock_entry.html',context={'form':form})
    else:
        return render(request,'bill_app/stock_entry.html',context={'form':form})
    

@login_required(login_url='')
def barcode_generate_view(request):
    form=GeneratecodeForm()
    if request.method =='POST':
        user=request.user
        form=GeneratecodeForm(request.POST)
        if form.is_valid():
            print('product no')
            # product=form.save()
            
            product_name=request.POST.get('product_name')
            p_brand=request.POST.get('brand')
            tq_units=request.POST.get('tq_units')
            p_unit=request.POST.get('q_measurements')
            
            if request.POST.get('manufacture_date') == '':
                manuf_date=None
            else:
                get_manuf_date=request.POST.get('manufacture_date')
                manuf_date=datetime.datetime.strptime(get_manuf_date, "%Y-%m-%d")
            
            if request.POST.get('expiry_date') == '':
                expiry=None
            else:
                get_expiry=request.POST.get('expiry_date')
                expiry=datetime.datetime.strptime(get_expiry, "%Y-%m-%d")
                
            if request.POST.get('total_quantity') == '':
                total_qty=float(0)
            else:
                try:
                    total_qty=float(request.POST.get('total_quantity'))
                except:
                    total_qty=float(0)
                    
            if request.POST.get('product_quantity')=='':
                product_qty=float(0)
            else:
                try:
                    product_qty=float(request.POST.get('product_quantity'))
                except:
                    product_qty=float(0)
            
            if request.POST.get('sale_price')=='':
                s_price=float(0)
            else:
                try:        
                    s_price=float(request.POST.get('sale_price'))
                except:
                    s_price=float(0)
            
            if request.POST.get('mrp')=='': 
                mrp=float(0)
            else:
                try:       
                    mrp=float(request.POST.get('mrp'))
                except:
                    mrp=float(0)
            
            if request.POST.get('purchase_amount')=='':
                purchase_amt=float(0)
            else:
                try:
                    purchase_amt=float(request.POST.get('purchase_amount'))
                except:
                    purchase_amt=float(0)
                    
            
            product001=AddProduct.objects.create(brand=p_brand,product_name=product_name,
                                            manufacture_date=manuf_date,expiry_date=expiry,total_quantity=total_qty,
                                            product_quantity=product_qty,tq_units=tq_units,
                                            q_measurements=p_unit,sale_price=s_price,mrp=mrp,purchase_amount=purchase_amt)

            while True:
                barcode_no=my_numb()
                print(f'first bar random number={barcode_no}')
                pro=product001.product_name
                gen=GenerateProduct.objects.create(barcode_no=barcode_no,product_name=pro)
                # gen.save()
                print('create super barcode')
                print(gen)
                
                g=gen.id
                print(f'id of object=={g}')
            
                img_bar=gen.bar_img_no
                img=str(img_bar)
                print(img_bar)

                lis=[]
                product_obj=AddProduct.objects.all()
                for product in product_obj:
                    check_no=product.barcode_no
                    print('inside for loop printing')
                    print(check_no)
                    if check_no == img:
                        lis.append(check_no)
                
                print(lis)
                
                if bool(lis)==False:
                    break
                else:
                    take_no=lis[0]
                    print(take_no)
                    if take_no==img:
                        gen.delete()
                        print('barcode delete')
                        continue
                    else:
                        print('its enter in else portion')
                        break
            
            print('after_condition')  
            bar=gen.bar_img_no
            
            product001.generate_product=gen
            product001.barcode_no=bar
            product001.generate=True
            q=product001.total_quantity
            p=product001.sale_price
            product001.cal_amount=float(q)*float(p)
            product001.user=user
            product001.stock_quantity=q
            product001.save()
            print('wow super')
            geting_id=gen.id
            print(geting_id)
            messages.success(request,'Product added successfully and generate barcode')
            # return redirect('barcode_generate_view')
            return redirect('barcode_printing',gen_id=geting_id)
        else:
            messages.error(request,'Invalid form entiry')
            return render(request,'bill_app/bar_gen.html',context={'form':form})
    else:
        return render(request,'bill_app/bar_gen.html',context={'form':form})


@login_required(login_url='')
def barcode_printing(request,gen_id=None):
    id=gen_id
    print(id)
    gen_product=GenerateProduct.objects.get(id=id)
    g_id=gen_product.id
    product=AddProduct.objects.get(generate_product_id=g_id)
    
    return render(request,'bill_app/barcode_printing.html',context={'gen_product':gen_product,'product':product})  

@login_required(login_url='')
def print_bar(request,product_id=None):
    p_id=product_id
    print(id)
    product=AddProduct.objects.get(id=p_id)
    g_id=product.generate_product_id
    gen_product=GenerateProduct.objects.get(id=g_id)
    return render(request,'bill_app/barcode_printing.html',context={'gen_product':gen_product,'product':product}) 
  
  
@login_required(login_url='')
def view_stock(request):
    all_products=AddProduct.objects.filter(active=True).order_by('-created_at')
    return render(request,'bill_app/view_products.html',context={'all_products':all_products})

@login_required(login_url='')
def view_barcode_page(request):
    all_products=AddProduct.objects.filter(active=True,generate=True).order_by('-created_at')
    return render(request,'bill_app/barcode.html',context={'all_products':all_products})



@login_required(login_url='')
def product_edit(request):
    if request.method =='POST':
        print('we enter the  link okkk')
        my=request.POST.get('rejin')
        id=request.POST.get('id')
        print(id)
        stock=AddProduct.objects.get(id=id)
        print(stock)
        stock_name=stock.product_name
        stock_brand=stock.brand
        stock_mg_date=stock.manufacture_date
        print(type(stock_mg_date))
        stock_expiry=stock.expiry_date
        stock_tq=stock.total_quantity
        stock_product_quty=stock.product_quantity
        stock_units=stock.q_measurements
        stock_sale_price=stock.sale_price
        stock_mrp=stock.mrp
        stock_purchase_amt=stock.purchase_amount
        stock_tq_unit=stock.tq_units
        
        if request.POST.get('product_name') == '':
            p_name=stock_name
        else:
            p_name=request.POST.get('product_name')
            
        if request.POST.get('brand')=='':
            brand=stock_brand
        else:
            brand=request.POST.get('brand')
            
        if request.POST.get('manufacture_date') == '':
            if stock_mg_date==None:
                manuf_date=None
            else:
                manuf_date=stock_mg_date
        else:
            get_manuf_date=request.POST.get('manufacture_date')
            manuf_date=datetime.datetime.strptime(get_manuf_date, "%Y-%m-%d")
            
        if request.POST.get('expiry_date') == '':
            if stock_expiry==None:
                expiry=None
            else:
                expiry=stock_expiry
        else:
            get_expiry=request.POST.get('expiry_date')
            expiry=datetime.datetime.strptime(get_expiry, "%Y-%m-%d")
            
            
            
        if request.POST.get('total_quantity') == '':
            if stock_tq == None:
                total_qty=float(0)
            else:
                total_qty=stock_tq
        elif request.POST.get('total_quantity') =='None':
            if stock_tq == None:
                total_qty=float(0)
            else:
                total_qty=stock_tq
        else:
            try:
                total_qty=float(request.POST.get('total_quantity'))     
            except:
                total_qty=float(0)
                print('summa')
        
            
        if request.POST.get('product_quantity') == '':
            if stock_product_quty==None:
                product_qty=float(0)
            else:
                product_qty=stock_product_quty
        elif request.POST.get('product_quantity') == 'None':
            if stock_product_quty==None:
                product_qty=float(0)
            else:
                product_qty=stock_product_quty
        else:
            try:
                product_qty=float(request.POST.get('product_quantity'))
            except:
                product_qty=float(0)
            
            
        if request.POST.get('q_measurements') =='':
            units=stock_units
        else:
            units=request.POST.get('q_measurements')
            
        if request.POST.get('tq_units') =='':
            tq_units=stock_tq_unit
        else:
            tq_units=request.POST.get('tq_units')
            
        if request.POST.get('sale_price') == '':
            if stock_sale_price==None:
                s_price=float(0)
            else:
                s_price=stock_sale_price
        elif request.POST.get('sale_price') == 'None':
            if stock_sale_price==None:
                s_price=float(0)
            else:
                s_price=stock_sale_price
        else:
            try:
                s_price=float(request.POST.get('sale_price'))
            except:
                s_price=float(0)
                
        if request.POST.get('mrp') == '':
            if stock_mrp==None:
                mrp=float(0)
            else:
                mrp=stock_mrp
        elif request.POST.get('mrp') == 'None':
            if stock_mrp==None:
                mrp=float(0)
            else:
                mrp=stock_mrp
        else:
            try:
                mrp=float(request.POST.get('mrp'))
            except:
                mrp=float(0)
            
        if request.POST.get('purchase_amount') == '':
            if stock_purchase_amt ==None:
                purchase_amt=float(0)
            else:
                purchase_amt=stock_purchase_amt
                
        elif request.POST.get('purchase_amount') == 'None':
            if stock_purchase_amt ==None:
                purchase_amt=float(0)
            else:
                purchase_amt=stock_purchase_amt
        else:
            try:
                purchase_amt=float(request.POST.get('purchase_amount'))
            except:
                purchase_amt=float(0)
        
       
                
        stock.product_name=p_name
        stock.brand=brand
        stock.manufacture_date=manuf_date
        stock.expiry_date=expiry
        stock.product_quantity=product_qty
        stock.q_measurements=units
        stock.sale_price=s_price
        stock.mrp=mrp
        stock.purchase_amount=purchase_amt
        stock.tq_units=tq_units
        stock.save()
        
        take_stockqty=stock.stock_quantity
        if stock.sold:
            print('Yes this product is sold')
            if total_qty > stock_tq:
                print('total qty greaterthan stock tq')
                find_diff=float(total_qty)-float(stock_tq)
                calculate_tq=float(stock_tq)+float(find_diff)
                calculate_the_stock_q=float(take_stockqty)+float(find_diff)
                stock.total_quantity=calculate_tq
                stock.stock_quantity=calculate_the_stock_q
                stock.save()
                
            elif total_qty == stock_tq:
                print('total qty equal stock tq')
                stock.total_quantity=total_qty
                stock.save()
            
            elif total_qty < stock_tq:
                print('total qty less than stock tq')
                cal_diff=float(stock_tq)-float(total_qty)
                cal_stock_thing=float(take_stockqty)-float(cal_diff)
                if cal_stock_thing <=0:
                    print('cal_stock_thing diff lessthen zero')
                else:
                    stock.total_quantity=total_qty
                    stock.stock_quantity=cal_stock_thing
                    stock.save()
                
            if total_qty == 0:
                print('tq is zero')
                stock.total_quantity=total_qty
                stock.stock_quantity=total_qty
                stock.save()
                
        else:
            print('this is not sold yet')
            stock.total_quantity=total_qty
            stock.stock_quantity=total_qty
            stock.save()
            
        today=datetime.datetime.now()
        check_expiry_date=stock.expiry_date
        if check_expiry_date != None:
            print('we enter from date condition')
            if today > check_expiry_date:
                print('today date greater than expiry date')
                stock.expiry=True
                stock.save()
            elif today == check_expiry_date:
                print('today date equal expiry date')
                stock.expiry=True
                stock.save()
            if check_expiry_date > today:
                print('expiry date greater than today date')
                stock.expiry=False
                stock.save()
            
        
        if stock.stock_quantity == 0:
            stock.out_of_stock=True
            stock.save()
        else:
            stock.out_of_stock=False
            stock.save()
        
        s_tq=stock.total_quantity   
        selling_price=stock.sale_price 
        cal_amount=float(s_tq) * float(selling_price)
        stock.cal_amount=cal_amount
        stock.save()
            
        print('object saved da')
        
        messages.success(request,'Edit product successfully')
        if my == 'True':
            return redirect('view_barcode_page')
        elif my == 'False':
            return redirect('view_stock')
    else:
        return redirect('view_stock')
        

@login_required(login_url='')
def bill_page(request):
    return render(request,'bill_app/bill_page.html')


# api checking
@login_required(login_url='')
# for checking
# @csrf_exempt
def check_api(request): 
    print('justice')
    data = request.POST.get('barcode_no')
    print(data)

    req_bar_obj=AddProduct.objects.filter(barcode_no=data,active=True,status=True)
    print(req_bar_obj)
    
    if req_bar_obj:
        print('ajay is coming')
        take_obj=AddProduct.objects.get(barcode_no=data)
        
        getting_id=take_obj.id
        print(getting_id)
        dic={}
        dic['product_name']=str(take_obj.product_name)
        dic['price']=str(take_obj.sale_price)
        dic['obj_id']=str(take_obj.id)
        dic['stock_qty']=str(take_obj.stock_quantity)
        dic['mrp']=str(take_obj.mrp)
        
        print(dic)  
        return JsonResponse(dic)
    else:
        dic2={'noname':"empty"}
        print(dic2)
        return JsonResponse(dic2)

@login_required(login_url='') 
# @csrf_exempt
def bill_submit(request):
    if request.method =='POST':
        user=request.user
        print(user)
        print('martian')
        data = json.load(request)
        datas=data['invoice']
        print (datas)
        print('rejin')
        con=datas['consulting']
        print(con)
        print('nothing')
        inv=con['Invoice']
        print(inv)
        
        total_amt=con['Total_Amt']
        print(total_amt)
        if total_amt == '':
            total_amt=0
        elif total_amt == 'NaN':
            total_amt=0
        else:
            total_amt=total_amt
            
        paymentt_mode=con['paymentt_mode']
        print(paymentt_mode)
        
        paid=con['amt_paid']
        print(paid)
        if paid == '' and total_amt == '':
            dic3={'martian':"empty"}
            print(dic3)
            return JsonResponse(dic3)
        elif paid == '':
            dic4={'martian':"empty"}
            print(dic4)
            return JsonResponse(dic4)
        elif total_amt == '':
            dic5={'martian':"empty"}
            print(dic5)
            return JsonResponse(dic5)
        else:
            if paid == '':
                paid=0
            elif paid == 'NaN':
                paid=0
            else:
                paid=paid
                
            balance=con['balance']
            print(balance)
            
            if balance == '':
                balance=0
            elif balance == 'NaN':
                balance=0
            else:
                balance=balance
                
            # total_items=con['total_items']
            # print(total_items)
            
            # if total_items == '':
            #     total_items=0
            # elif total_items == 'NaN':
            #     total_items=0
            # else:
            #     total_items=total_items
                
            # savings=con['savings']
            # print(savings)
            
            # if savings == '':
            #     savings=0
            # elif savings == 'NaN':
            #     savings=0
            # else:
            #     savings=savings
            
            create_invoice=SalesInvoice.objects.create(user=user,sales_bill_no=bill_no(),grand_total=total_amt,amount_received=paid,
                                                    balance_return=balance,payment_type=paymentt_mode)
            
            # create_invoice=SalesInvoice.objects.create(user=user,sales_bill_no=bill_no(),grand_total=total_amt,amount_received=paid,
            #                                         balance_return=balance,payment_type=paymentt_mode,
            #                                          total_items=total_items,savings=savings)
            
            invoice_id=create_invoice.id
            
            items_list=[]
            
            mrp_amt_list=[]
            
            for invoice in inv:
                barcode=invoice['Barcode']
                print(barcode)
                p_name=invoice['Name']
                print(p_name)
                quantity=invoice['Quantity']
                print(quantity)
                
                if quantity == '':
                    quantity=0
                elif quantity == 'NaN':
                    quantity=0
                else:
                    quantity=quantity
                    
                print(type(quantity))
                
                mrp001=invoice['MRP']
                print(mrp001)
                
                if mrp001 == '':
                    mrp001=0
                elif mrp001 == 'NaN':
                    mrp001=0
                else:
                    mrp001=mrp001
                
                pr=invoice['Price']
                print(pr)
                
                if pr == '':
                    pr=0
                elif pr == 'NaN':
                    pr=0
                else:
                    pr=pr
                    
                cal_total=invoice['Total']
                print(cal_total)
                
                if cal_total == '':
                    cal_total=0
                elif cal_total == 'NaN':
                    cal_total=0
                else:
                    cal_total=cal_total
                
                try:
                    get_product=AddProduct.objects.get(barcode_no=barcode)
                    print(get_product)
                    s_quanty=get_product.stock_quantity
                    sold_qty=get_product.sold_quantity
                    calculate_quantity=float(s_quanty)-float(quantity)
                    if calculate_quantity <= 0:
                        print('quantity equal to zero')
                        get_product.out_of_stock=True
                        get_product.stock_quantity=calculate_quantity
                        get_product.sold=True
                        get_product.sold_quantity=float(sold_qty)+float(quantity)
                        get_product.save()
                    else:
                        get_product.stock_quantity=calculate_quantity
                        get_product.sold=True
                        get_product.sold_quantity=float(sold_qty)+float(quantity)
                        get_product.save()
                        
                    sale_product=SalesProduct.objects.create(invoice=create_invoice,product=get_product,sale_quantity=quantity,
                                                price=pr,total_amount=cal_total)

                    
                    take_sale_qty=sale_product.sale_quantity
                    print(take_sale_qty)
                    print(type(take_sale_qty))
                    items_list.append(float(take_sale_qty))
                    take_mrp=get_product.mrp
                    cal_saving=float(take_sale_qty) * float(take_mrp)
                    mrp_amt_list.append(float(cal_saving))
                    
                    sale_product.mrp=take_mrp
                    sale_product.save()
                
                except:
                    sale_product001=SalesProduct.objects.create(invoice=create_invoice,sale_quantity=quantity,mrp=mrp001,
                            price=pr,total_amount=cal_total,enter_product=p_name)
                    
                    take_sale_qty001=sale_product001.sale_quantity
                    print(take_sale_qty001)
                    print(type(take_sale_qty001))
                    items_list.append(float(take_sale_qty001))
                    
                    cal_saving001=float(take_sale_qty001) * float(mrp001)
                    mrp_amt_list.append(float(cal_saving001))
                    
                    
                    
            
            cal_total_items=sum(items_list)
            print(f'number of items= {cal_total_items}')
            
            cal_mrp_amt_list=sum(mrp_amt_list)
            print(cal_mrp_amt_list)
            get_total=create_invoice.grand_total
            cal_saving_diff=float(cal_mrp_amt_list) - float(get_total)
            print(cal_saving_diff)
            
            create_invoice.total_items=cal_total_items
            create_invoice.savings=cal_saving_diff
            create_invoice.save()
            
            dic={'bill_id':invoice_id}
            return JsonResponse(dic)
            # return JsonResponse(datas)
            # return redirect('print_bill',in_id=invoice_id)
 
    else:
        return redirect('bill_page')
    
    
@login_required(login_url='')
def print_bill(request,in_id=None):
    id=in_id
    print(id)
    get_invoice=SalesInvoice.objects.get(id=id)
    print(get_invoice)
    sales_product_object=SalesProduct.objects.filter(invoice_id=id)
    # sales_product_object=[SalesProduct.objects.get(id=i.id) for i in SalesProduct.objects.filter(invoice_id=id) if i.total_amount >0]
    print(sales_product_object)
    return render(request,'bill_app/print_bill.html',context={'sales_product_object':sales_product_object,'get_invoice':get_invoice})


@login_required(login_url='')
def view_sales_details(request):
    invoice=SalesInvoice.objects.all().order_by('-created_at')
    return render(request,'bill_app/view_sales_details.html',{'invoice':invoice})

@login_required(login_url='')
def view_bill(request):
    if request.method == 'POST':
        id =request.POST.get('id')
        print(id)
        get_invoice=SalesInvoice.objects.get(id=id)
        print(get_invoice)
        sales_product_object=SalesProduct.objects.filter(invoice_id=id)
        # sales_product_object=[SalesProduct.objects.get(id=i.id) for i in SalesProduct.objects.filter(invoice_id=id) if i.total_amount >0]
        print(sales_product_object)
        return render(request,'bill_app/view_bills.html',context={'sales_product_object':sales_product_object,'get_invoice':get_invoice})
    else:
        return redirect('view_sales_details')
        
    
@login_required(login_url='')
def product_disable_view(request):
    if request.method =='POST':
        id=request.POST.get('id')
        my_object=AddProduct.objects.get(id=id)
        my_object.status=False
        my_object.save()
        messages.success(request,'Product disabled successfully')
        return redirect('view_stock')
    else:
        return redirect('view_stock')
        

@login_required(login_url='')
def product_enable_view(request):
    if request.method =='POST':
        id=request.POST.get('id')
        my_object=AddProduct.objects.get(id=id)
        my_object.status=True
        my_object.save()
        messages.success(request,'Product Enabled successfully')
        return redirect('view_stock')
    else:
        return redirect('view_stock')
    

@login_required(login_url='')
def product_remove(request):
    if request.method =='POST':
        id=request.POST.get('id')
        my_object=AddProduct.objects.get(id=id)
        # my_object.active=False
        # my_object.status=False
        # my_object.save()
        my_object.delete()
        messages.success(request,'Product Removed successfully')
        return redirect('view_stock')
    else:
        return redirect('view_stock')


@login_required(login_url='')
def product_readd(request):
    if request.method =='POST':
        id=request.POST.get('id')
        my_object=AddProduct.objects.get(id=id)
        my_object.active=True
        my_object.status=True
        my_object.save()
        messages.success(request,'Product Readded successfully')
        return redirect('remove_product_view')
    else:
        return redirect('remove_product_view') 
    
@login_required(login_url='')
def remove_product_view(request):
    all_products=AddProduct.objects.filter(active=False)
    return render(request,'bill_app/remove_product.html',context={'all_products':all_products})

@login_required(login_url='')
def expired_product_view(request):
    all_products=AddProduct.objects.filter(expiry=True)
    return render(request,'bill_app/expired.html',context={'all_products':all_products})

@login_required(login_url='')
def edit_page_view(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        rejin=request.POST.get('rejin')
        product=AddProduct.objects.get(id=id)
        return render(request,'bill_app/edit.html',{'product':product,'rejin':rejin})
    else:
        return redirect('view_stock')

        
    
    

        


