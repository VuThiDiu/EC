# Generated by Django 3.0.8 on 2020-11-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSV', '0006_collect_order_orderdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
