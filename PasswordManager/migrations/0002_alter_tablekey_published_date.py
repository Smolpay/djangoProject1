# Generated by Django 3.2.6 on 2021-09-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PasswordManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablekey',
            name='published_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
