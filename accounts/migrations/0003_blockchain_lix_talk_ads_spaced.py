# Generated by Django 3.1.7 on 2022-05-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_defi_talk_twi_defi_talk_twi_ads'),
    ]

    operations = [
        migrations.CreateModel(
            name='blockchain_LIX_talk_ads_spaced',
            fields=[
                ('Row_id', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.TextField()),
                ('Last_Name', models.TextField()),
                ('Description', models.TextField()),
                ('Profile_Link', models.TextField()),
                ('Email_id', models.TextField()),
                ('Location', models.TextField()),
                ('Category', models.TextField()),
                ('contact', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
