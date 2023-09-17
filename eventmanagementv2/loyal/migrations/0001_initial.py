# Generated by Django 4.2.5 on 2023-09-17 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=69, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=69)),
                ('firstName', models.CharField(max_length=100)),
                ('middleName', models.CharField(max_length=100, null=True)),
                ('lastName', models.CharField(max_length=100)),
                ('typeOfUser', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='loyal.user')),
                ('course', models.CharField(max_length=69)),
                ('year', models.IntegerField(default=1, max_length=1)),
                ('department', models.CharField(max_length=100)),
            ],
            bases=('loyal.user',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='loyal.user')),
                ('age', models.IntegerField(default=1, max_length=2)),
            ],
            bases=('loyal.user',),
        ),
        migrations.CreateModel(
            name='TeacherSpecialization',
            fields=[
                ('teacher_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='loyal.teacher')),
                ('specialization', models.CharField(max_length=69)),
            ],
            bases=('loyal.teacher',),
        ),
    ]
