# Generated by Django 3.2 on 2021-06-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0002_itemmodel_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCodeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo', models.CharField(max_length=128)),
                ('discount', models.CharField(max_length=128)),
            ],
        ),
    ]