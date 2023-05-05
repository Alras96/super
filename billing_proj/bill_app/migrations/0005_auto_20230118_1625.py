# Generated by Django 3.2.9 on 2023-01-18 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bill_app', '0004_addproduct_stock_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenerateProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode_no', models.CharField(max_length=255, null=True, unique=True)),
                ('barcode', models.ImageField(blank=True, upload_to='images/')),
                ('product_name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='addproduct',
            name='generate_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bill_app.generateproduct'),
        ),
    ]
