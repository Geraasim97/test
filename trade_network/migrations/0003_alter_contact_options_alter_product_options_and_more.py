# Generated by Django 4.2.3 on 2023-07-13 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_network', '0002_product_selling_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'contact', 'verbose_name_plural': 'contacts'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'model'], 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='memder_id',
            new_name='memder',
        ),
    ]