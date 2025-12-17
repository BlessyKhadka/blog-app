from django.db import migrations

def create_demo_posts(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Post = apps.get_model("blog", "Post")

    # Create demo user
    user, created = User.objects.get_or_create(
        username="demo_user",
        defaults={"email": "demo@example.com"},
    )
    user.set_password("password123")
    user.save()

    # Create demo posts if none exist
    if Post.objects.count() == 0:
        Post.objects.create(
            title="My First Blog Post",
            body="This is my first blog post deployed on Render using Django.",
            author=user,
        )
        Post.objects.create(
            title="What I Learned",
            body="I learned how to deploy Django, fix static files, and work with migrations.",
            author=user,
        )

class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_demo_posts),
    ]
