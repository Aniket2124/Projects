# Generated by Django 4.2.14 on 2024-08-21 05:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
