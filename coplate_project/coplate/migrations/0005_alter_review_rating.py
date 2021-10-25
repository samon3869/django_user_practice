# Generated by Django 3.2.8 on 2021-10-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0004_review_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=None),
        ),
    ]
