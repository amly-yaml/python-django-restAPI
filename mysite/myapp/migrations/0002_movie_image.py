# Generated by Django 4.0.3 on 2022-03-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='images/none/sample.jpgp', upload_to='images'),
        ),
    ]
