# Generated by Django 5.0.1 on 2024-05-16 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_actionhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionhistory',
            name='action',
            field=models.CharField(choices=[('add', 'Add'), ('delete', 'Delete'), ('update', 'Update')], max_length=10),
        ),
        migrations.AlterField(
            model_name='actionhistory',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.post'),
        ),
    ]