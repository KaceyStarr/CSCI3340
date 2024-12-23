# Generated by Django 5.1.3 on 2024-11-25 19:02

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
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the task', max_length=200)),
                ('description', models.TextField(blank=True, help_text='Detailed description of the task', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the task was created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the task was last updated')),
                ('due_date', models.DateTimeField(blank=True, help_text='Optional due date for the task', null=True)),
                ('is_completed', models.BooleanField(default=False, help_text='Mark task as completed')),
                ('user', models.ForeignKey(help_text='The user this task belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='todos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'To-Do Item',
                'verbose_name_plural': 'To-Do Items',
                'ordering': ['is_completed', 'due_date'],
            },
        ),
    ]
