# Generated by Django 3.2.19 on 2023-05-04 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='../ci-nft-social-hub/default_post_icenjp.jpg', upload_to='images/')),
                ('category_filter', models.CharField(choices=[('pfps / avatars', 'PFPs / Avatars'), ('one-of-one artwork', 'One-of-one Artwork'), ('generative art', 'Generative art'), ('collectibles', 'Collectibles'), ('photography', 'Photography'), ('music', 'Music'), ('gamified', 'Gameified'), ('event ticket', 'Event Ticket'), ('membership pass', 'Membership Pass'), ('domain names', 'Domain names'), ('other', 'Other')], default='normal', max_length=32)),
                ('website', models.URLField(blank=True)),
                ('social', models.URLField(blank=True)),
                ('marketplace', models.URLField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
