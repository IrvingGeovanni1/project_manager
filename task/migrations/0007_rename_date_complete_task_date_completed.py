# Generated by Django 5.0.3 on 2024-03-21 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_rename_update_at_task_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date_complete',
            new_name='date_completed',
        ),
    ]