# Generated by Django 5.0.1 on 2024-05-16 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_actionhistory_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actionhistory',
            name='date',
        ),
    ]