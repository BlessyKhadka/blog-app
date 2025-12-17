from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_demo_posts(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Post = apps.get_model("blog", "Post")

    # Create demo user (password must be hashed in migrations)
    user, created = User.objects.get_or_create(
        username="demo_user",
        defaults={
            "email": "demo@example.com",
            "password": make_password("password123"),
        },
    )

    # Create demo posts only if none exist
    if Post.objects.count() == 0:
        Post.objects.create(
            title="My First Blog Post",
            body="This is my first blog post deployed on Render using Django.",
            author=user,
        )
        Post.objects.create(
            title="What I Learned",
            body="I learned Django models, URLs, templates, Git, and deployment.",
            author=user,
        )

class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_demo_posts),
    ]
