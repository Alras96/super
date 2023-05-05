# Generated by Django 4.1.5 on 2023-01-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_app', '0006_auto_20230118_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproduct',
            name='generate',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='addproduct',
            name='q_measurements',
            field=models.CharField(choices=[('ML', 'ML'), ('LITRE', 'LITRE'), ('GRAM', 'GRAM'), ('KG', 'KG'), ('PIECES', 'PIECES')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='generateproduct',
            name='bar_img_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generateproduct',
            name='barcode_no',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
