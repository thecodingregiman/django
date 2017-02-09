# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_alt_id', models.CharField(max_length=50, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('cell_phone', models.CharField(default='###-###-####', max_length=20, null=True)),
                ('instructor_picture', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor_in_lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneplace.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_alt_id', models.CharField(max_length=50, null=True)),
                ('class_name', models.CharField(max_length=60)),
                ('class_description', models.TextField(max_length=500)),
                ('class_capacity', models.IntegerField(blank=True, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('instructor_members', models.ManyToManyField(through='oneplace.Instructor_in_lesson', to='oneplace.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=50)),
                ('level_description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_alt_id', models.CharField(max_length=50, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('cell_phone', models.CharField(default='###-###-####', max_length=20, null=True)),
                ('student_picture', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Student_in_lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneplace.Lesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneplace.Student')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oneplace.Lesson_level'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='student_members',
            field=models.ManyToManyField(through='oneplace.Student_in_lesson', to='oneplace.Student'),
        ),
        migrations.AddField(
            model_name='instructor_in_lesson',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneplace.Lesson'),
        ),
        migrations.AlterUniqueTogether(
            name='student_in_lesson',
            unique_together=set([('student', 'lesson')]),
        ),
        migrations.AlterUniqueTogether(
            name='instructor_in_lesson',
            unique_together=set([('instructor', 'lesson')]),
        ),
    ]