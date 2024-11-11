# Generated by Django 5.0.6 on 2024-06-27 12:44

import backupss.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='new folder', max_length=50)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=False)),
                ('is_shared', models.BooleanField(default=False)),
                ('shared_at', models.DateTimeField(auto_now_add=True)),
                ('is_trashed', models.BooleanField(default=False)),
                ('trashed_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_starred', models.BooleanField(default=False)),
                ('starred_at', models.DateTimeField(blank=True, null=True)),
                ('is_encrypted', models.BooleanField(default=False)),
                ('encrypted_at', models.DateTimeField(blank=True, null=True)),
                ('is_locked', models.BooleanField(default=False)),
                ('locked_at', models.DateTimeField(blank=True, null=True)),
                ('is_protected', models.BooleanField(default=False)),
                ('protected_at', models.DateTimeField(blank=True, null=True)),
                ('shared_with', models.ManyToManyField(blank=True, related_name='shared_with', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('file', models.FileField(upload_to=backupss.models.user_directory_path)),
                ('is_public', models.BooleanField(default=False)),
                ('is_shared', models.BooleanField(default=False)),
                ('shared_at', models.DateTimeField(auto_now_add=True)),
                ('is_trashed', models.BooleanField(default=False)),
                ('trashed_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_starred', models.BooleanField(default=False)),
                ('starred_at', models.DateTimeField(blank=True, null=True)),
                ('is_encrypted', models.BooleanField(default=False)),
                ('encrypted_at', models.DateTimeField(blank=True, null=True)),
                ('is_locked', models.BooleanField(default=False)),
                ('locked_at', models.DateTimeField(blank=True, null=True)),
                ('is_protected', models.BooleanField(default=False)),
                ('protected_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='backupss.folder')),
            ],
        ),
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Image', max_length=150)),
                ('image', models.ImageField(upload_to=backupss.models.user_image_directory_path)),
                ('is_trashed', models.BooleanField(default=False)),
                ('trashed_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_starred', models.BooleanField(default=False)),
                ('starred_at', models.DateTimeField(blank=True, null=True)),
                ('is_encrypted', models.BooleanField(default=False)),
                ('encrypted_at', models.DateTimeField(blank=True, null=True)),
                ('is_locked', models.BooleanField(default=False)),
                ('locked_at', models.DateTimeField(blank=True, null=True)),
                ('is_protected', models.BooleanField(default=False)),
                ('protected_at', models.DateTimeField(blank=True, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('is_shared', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='backupss.folder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
