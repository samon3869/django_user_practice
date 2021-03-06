# Generated by Django 3.2.8 on 2021-10-26 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0005_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='intro',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics'),
        ),
    ]
