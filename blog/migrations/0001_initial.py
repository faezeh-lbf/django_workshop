# Generated by Django 3.1.5 on 2021-01-14 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, help_text='برای نمایش بهتر در سایت، باید نسبت ابعاد تصویر بین ۰.۸ تا ۱.۲ باشد.', null=True, upload_to='blog/')),
                ('title', models.CharField(max_length=70)),
                ('summary', models.TextField(max_length=100)),
                ('publish_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('author_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date_time', models.DateTimeField()),
                ('show', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost')),
            ],
        ),
    ]