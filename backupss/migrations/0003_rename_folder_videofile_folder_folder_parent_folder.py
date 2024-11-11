# Generated by Django 5.0.6 on 2024-07-14 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backupss', '0002_videofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videofile',
            old_name='Folder',
            new_name='folder',
        ),
        migrations.AddField(
            model_name='folder',
            name='parent_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subfolders', to='backupss.folder'),
        ),
    ]
