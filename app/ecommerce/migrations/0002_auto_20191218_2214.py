# Generated by Django 3.0 on 2019-12-18 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Profile/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='pictute',
            field=models.ImageField(upload_to='Product/'),
        ),
        migrations.AlterField(
            model_name='instagram',
            name='image',
            field=models.ImageField(upload_to='Instagram/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='Product/'),
        ),
    ]
