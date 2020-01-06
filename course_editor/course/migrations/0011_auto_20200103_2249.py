# Generated by Django 3.0.1 on 2020-01-03 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_course_source_language_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnword',
            name='image1',
            field=models.TextField(choices=[('pasta1', 'pasta1'), ('pasta2', 'pasta2'), ('pasta3', 'pasta3'), ('bread1', 'bread1'), ('bread2', 'bread2'), ('bread3', 'bread3'), ('milk1', 'milk1'), ('milk2', 'milk2'), ('milk3', 'milk3'), ('sky1', 'sky1'), ('sky2', 'sky2'), ('sky3', 'sky3'), ('people1', 'people1'), ('people2', 'people2'), ('people3', 'people3'), ('couple1', 'couple1'), ('couple2', 'couple2'), ('couple3', 'couple3'), ('student1', 'student1'), ('student2', 'student2'), ('student3', 'student3'), ('lion1', 'lion1'), ('lion2', 'lion2'), ('lion3', 'lion3'), ('duck1', 'duck1'), ('duck2', 'duck2'), ('duck3', 'duck3'), ('dog1', 'dog1'), ('dog2', 'dog2'), ('dog3', 'dog3'), ('cat1', 'cat1'), ('cat2', 'cat2'), ('cat3', 'cat3'), ('bear1', 'bear1'), ('bear2', 'bear2'), ('bear3', 'bear3'), ('woman1', 'woman1'), ('woman2', 'woman2'), ('woman3', 'woman3'), ('man1', 'man1'), ('man2', 'man2'), ('man3', 'man3')], default='cat1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learnword',
            name='image2',
            field=models.TextField(choices=[('pasta1', 'pasta1'), ('pasta2', 'pasta2'), ('pasta3', 'pasta3'), ('bread1', 'bread1'), ('bread2', 'bread2'), ('bread3', 'bread3'), ('milk1', 'milk1'), ('milk2', 'milk2'), ('milk3', 'milk3'), ('sky1', 'sky1'), ('sky2', 'sky2'), ('sky3', 'sky3'), ('people1', 'people1'), ('people2', 'people2'), ('people3', 'people3'), ('couple1', 'couple1'), ('couple2', 'couple2'), ('couple3', 'couple3'), ('student1', 'student1'), ('student2', 'student2'), ('student3', 'student3'), ('lion1', 'lion1'), ('lion2', 'lion2'), ('lion3', 'lion3'), ('duck1', 'duck1'), ('duck2', 'duck2'), ('duck3', 'duck3'), ('dog1', 'dog1'), ('dog2', 'dog2'), ('dog3', 'dog3'), ('cat1', 'cat1'), ('cat2', 'cat2'), ('cat3', 'cat3'), ('bear1', 'bear1'), ('bear2', 'bear2'), ('bear3', 'bear3'), ('woman1', 'woman1'), ('woman2', 'woman2'), ('woman3', 'woman3'), ('man1', 'man1'), ('man2', 'man2'), ('man3', 'man3')], default='cat2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learnword',
            name='image3',
            field=models.TextField(choices=[('pasta1', 'pasta1'), ('pasta2', 'pasta2'), ('pasta3', 'pasta3'), ('bread1', 'bread1'), ('bread2', 'bread2'), ('bread3', 'bread3'), ('milk1', 'milk1'), ('milk2', 'milk2'), ('milk3', 'milk3'), ('sky1', 'sky1'), ('sky2', 'sky2'), ('sky3', 'sky3'), ('people1', 'people1'), ('people2', 'people2'), ('people3', 'people3'), ('couple1', 'couple1'), ('couple2', 'couple2'), ('couple3', 'couple3'), ('student1', 'student1'), ('student2', 'student2'), ('student3', 'student3'), ('lion1', 'lion1'), ('lion2', 'lion2'), ('lion3', 'lion3'), ('duck1', 'duck1'), ('duck2', 'duck2'), ('duck3', 'duck3'), ('dog1', 'dog1'), ('dog2', 'dog2'), ('dog3', 'dog3'), ('cat1', 'cat1'), ('cat2', 'cat2'), ('cat3', 'cat3'), ('bear1', 'bear1'), ('bear2', 'bear2'), ('bear3', 'bear3'), ('woman1', 'woman1'), ('woman2', 'woman2'), ('woman3', 'woman3'), ('man1', 'man1'), ('man2', 'man2'), ('man3', 'man3')], default='cat3'),
            preserve_default=False,
        ),
    ]
