# Generated by Django 5.1 on 2024-08-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Appetizer', 'Appetizer'), ('Entree', 'Entree'), ('Beverage', 'Beverage'), ('Dessert', 'Dessert')], max_length=100),
        ),
    ]
