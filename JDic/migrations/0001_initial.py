# Generated by Django 2.1.1 on 2018-09-28 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kanjis', models.CharField(max_length=256)),
                ('meaning', models.CharField(max_length=256)),
                ('kun', models.CharField(max_length=256)),
                ('on', models.CharField(max_length=256)),
            ],
        ),
    ]