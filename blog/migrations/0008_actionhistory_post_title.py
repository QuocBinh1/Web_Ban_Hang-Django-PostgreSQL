# Generated by Django 5.0.1 on 2024-05-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_actionhistory_action_alter_actionhistory_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionhistory',
            name='post_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
