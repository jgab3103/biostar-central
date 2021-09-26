# Generated by Django 3.1 on 2021-03-22 15:30

from django.db import migrations


def change_spam(apps, schema_editor):
    """
    Change all spam status to Post.CLOSED.
    """
    Post = apps.get_model('forum', 'Post')

    # Possible spam states.
    SPAM, NOT_SPAM, DEFAULT = range(3)
    # Post statuses.
    PENDING, OPEN, OFFTOPIC, CLOSED, DELETED = range(5)

    spam = Post.objects.filter(spam=SPAM)

    for s in spam:
        s.status = CLOSED
        s.save()


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='last_contributor',
        ),
    migrations.RunPython(change_spam),
    ]