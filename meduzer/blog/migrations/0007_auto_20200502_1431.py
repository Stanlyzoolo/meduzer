# Generated by Django 3.0.5 on 2020-05-02 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0006_auto_20200426_2001"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="annotation",
            field=models.TextField(blank=True, db_index=True, max_length=600),
        ),
        migrations.AddField(
            model_name="post",
            name="bibliography",
            field=models.CharField(blank=True, db_index=True, max_length=600),
        ),
        migrations.AddField(
            model_name="post",
            name="findings",
            field=models.CharField(blank=True, db_index=True, max_length=600),
        ),
        migrations.AddField(
            model_name="post",
            name="post_keywords",
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
        migrations.AddField(
            model_name="post",
            name="post_subject",
            field=models.CharField(db_index=True, default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blog_posts",
                related_query_name="post",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                allow_unicode=True,
                blank=True,
                max_length=150,
                unique=True,
                unique_for_date="publish",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(
                db_index=True, help_text=True, max_length=255, unique=True
            ),
        ),
    ]
