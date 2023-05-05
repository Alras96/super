# Generated by Django 3.2.9 on 2023-01-17 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bill_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_number', models.CharField(max_length=255, null=True, unique=True)),
                ('barcode_no', models.CharField(max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('product_name', models.CharField(max_length=255, null=True)),
                ('manufacture_date', models.DateTimeField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=300, null=True)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=300, null=True)),
                ('mrp', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True)),
                ('purchase_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True)),
                ('cal_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True)),
                ('active', models.BooleanField(default=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('expiry', models.BooleanField(default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_bill_no', models.CharField(blank=True, max_length=200, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True)),
                ('total_balance', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True)),
                ('balance_return', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True)),
                ('payment_type', models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Card', 'Card'), ('UPI', 'UPI')], max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_quantity', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bill_app.salesinvoice')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bill_app.addproduct')),
            ],
        ),
    ]