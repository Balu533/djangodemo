# Generated by Django 2.2.5 on 2019-12-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_bookinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]