from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.login_view,name='login'),
    path('admin_register',views.admin_register,name='admin_register'),
    path('user_register',views.user_register,name='user_register'),
    
    path('update_password',views.update_password,name='update_password'),
    path('change_password',views.change_password,name='change_password'),
    
    
    
    path('logout',views.user_logout,name='logout'),
    path('home',views.home_view,name='home'),
    
    # users thing
    path('view_users',views.view_users,name='view_users'),
    path('disable_view',views.disable_view, name='disable_view'),
    path('enable_view',views.enable_view, name='enable_view'),
    
    path('stock_entry',views.stock_entry, name='stock_entry'),
    path('barcode_generate_view',views.barcode_generate_view, name='barcode_generate_view'),
    
    path('barcode_printing/<int:gen_id>',views.barcode_printing, name='barcode_printing'),
    
    
    path('view_stock',views.view_stock, name='view_stock'),
    path('product_disable_view',views.product_disable_view, name='product_disable_view'),
    path('product_enable_view',views.product_enable_view, name='product_enable_view'),
    path('product_remove',views.product_remove, name='product_remove'),
    path('product_readd',views.product_readd, name='product_readd'),
    path('remove_product_view',views.remove_product_view, name='remove_product_view'),
    path('product_edit',views.product_edit, name='product_edit'),
    
    path('view_barcode_page',views.view_barcode_page, name='view_barcode_page'),
    path('print_bar/<int:product_id>',views.print_bar, name='print_bar'),
    
    
    path('bill_page',views.bill_page, name='bill_page'),
    path('view_sales_details',views.view_sales_details, name='view_sales_details'),
    path('view_bill',views.view_bill, name='view_bill'),
    
    
    # api checking
    path('check_api',views.check_api, name='check_api'),
    path('bill_submit',views.bill_submit, name='bill_submit'),
    
    path('print_bill/<int:in_id>',views.print_bill, name='print_bill'),
    
    path('expired_product_view',views.expired_product_view, name='expired_product_view'),
    
    path('edit_page_view',views.edit_page_view, name='edit_page_view'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

