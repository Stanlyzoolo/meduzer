# Generated by Django 3.0.4 on 2020-03-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="post",
            name="body",
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(db_index=True, max_length=250),
        ),
        migrations.RemoveField(model_name="post", name="tags"),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="posts", to="blog.Tag"
            ),
        ),
    ]
