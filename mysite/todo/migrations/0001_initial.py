# Generated by Django 2.1.2 on 2018-11-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100, verbose_name='タスク')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
        ),
    ]
