# Generated by Django 3.0.7 on 2020-06-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_email',
            field=models.EmailField(default='test@example.com', max_length=50),
        ),
    ]
