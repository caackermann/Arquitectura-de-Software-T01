# Generated by Django 2.1.1 on 2018-09-12 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='client_ip',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
