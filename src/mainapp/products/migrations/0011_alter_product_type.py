# Generated by Django 5.1 on 2024-08-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Beverage', 'Beverage'), ('Entree', 'Entree'), ('Appetizer', 'Appetizer'), ('Dessert', 'Dessert')], max_length=100),
        ),
    ]
