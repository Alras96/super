# Generated by Django 4.1.5 on 2023-01-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_app', '0011_addproduct_sold_addproduct_sold_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesinvoice',
            name='savings',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True),
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='total_items',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='salesproduct',
            name='mrp',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=300, null=True),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='mrp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=300, null=True),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='q_measurements',
            field=models.CharField(choices=[('ML', 'ML'), ('Litre', 'Litre'), ('Grams', 'Grams'), ('Kg', 'Kg'), ('Pcs', 'Pcs')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='tq_units',
            field=models.CharField(choices=[('Litre', 'Litre'), ('Kg', 'Kg'), ('Pcs', 'Pcs')], max_length=255, null=True),
        ),
    ]
