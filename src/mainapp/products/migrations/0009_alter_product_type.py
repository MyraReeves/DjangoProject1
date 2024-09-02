# Generated by Django 5.1 on 2024-08-14 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Entree', 'Entree'), ('Dessert', 'Dessert'), ('Appetizer', 'Appetizer'), ('Beverage', 'Beverage')], max_length=100),
        ),
    ]
