# Generated by Django 3.1.5 on 2021-02-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210113_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men Fashion', 'Men Fashion'), ('Women Fashion', 'Women Fashion'), ('Electronics', 'Electronics'), ('Gagets', 'Gagets')], max_length=50),
        ),
    ]