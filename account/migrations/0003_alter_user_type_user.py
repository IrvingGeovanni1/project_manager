# Generated by Django 5.0.3 on 2024-04-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.CharField(choices=[('free', 'Free'), ('premium', 'Premium')], default='free', max_length=50),
        ),
    ]
