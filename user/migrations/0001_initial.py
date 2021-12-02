# Generated by Django 2.2 on 2021-11-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='İsim')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11, verbose_name='Telefon')),
                ('message', models.TextField(verbose_name='Mesaj')),
            ],
        ),
    ]