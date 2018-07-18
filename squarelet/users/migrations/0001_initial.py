# Generated by Django 2.0.6 on 2018-06-25 15:32

from django.db import migrations, models
import django.utils.timezone
import squarelet.core.fields
import squarelet.users.managers
import squarelet.users.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [("auth", "0009_alter_user_last_name_max_length")]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="name of user"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unqiue": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and ./+/-/_ only",
                        max_length=150,
                        unique=True,
                        validators=[squarelet.users.validators.UsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "created_at",
                    squarelet.core.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created at",
                    ),
                ),
                (
                    "updated_at",
                    squarelet.core.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="updated at",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"abstract": False},
            managers=[("objects", squarelet.users.managers.UserManager())],
        )
    ]
