# Generated by Django 4.2.5 on 2023-10-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('msg', models.CharField(max_length=200)),
            ],
        ),
    ]
