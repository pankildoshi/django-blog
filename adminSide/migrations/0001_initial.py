# Generated by Django 4.0.2 on 2022-04-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminName', models.CharField(max_length=200)),
                ('adminPassword', models.CharField(max_length=50)),
            ],
        ),
    ]