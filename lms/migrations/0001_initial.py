# Generated by Django 4.0.4 on 2022-05-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=100)),
                ('password', models.TextField()),
                ('User_type', models.TextField()),
            ],
        ),
    ]
