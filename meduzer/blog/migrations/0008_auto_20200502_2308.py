# Generated by Django 3.0.5 on 2020-05-02 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0007_auto_20200502_1431"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="tags",),
        migrations.AlterField(
            model_name="post",
            name="annotation",
            field=models.TextField(
                blank=True, db_index=True, max_length=600, null=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blog_posts",
                related_query_name="post",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Авторство",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="bibliography",
            field=models.CharField(
                blank=True, db_index=True, max_length=600, null=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="body",
            field=models.TextField(
                blank=True, db_index=True, null=True, verbose_name="Основная часть"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="findings",
            field=models.CharField(
                blank=True, db_index=True, max_length=600, null=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="post_keywords",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                allow_unicode=True,
                blank=True,
                max_length=150,
                null=True,
                unique=True,
                unique_for_date="publish",
            ),
        ),
    ]