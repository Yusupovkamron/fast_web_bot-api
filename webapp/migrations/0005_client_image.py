# Generated by Django 5.0.6 on 2024-06-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_rename_blog_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='image',
            field=models.ImageField(default=1, upload_to='webapp/client/'),
            preserve_default=False,
        ),
    ]
