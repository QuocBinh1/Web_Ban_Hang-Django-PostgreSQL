# Generated by Django 5.0.1 on 2024-04-07 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='postForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
