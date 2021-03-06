# Generated by Django 3.1.3 on 2020-11-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essportfolioapp', '0004_auto_20201130_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('technology', models.CharField(max_length=250)),
            ],
        ),
    ]
