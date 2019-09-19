# Generated by Django 2.1.7 on 2019-09-19 20:01

import autoslug.fields
from django.conf import settings
import django.contrib.postgres.fields.citext
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sorl.thumbnail.fields
import squarelet.core.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_organizationchangelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='charge_id',
            field=models.CharField(help_text='The strip ID for the charge', max_length=255, unique=True, verbose_name='charge_id'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='created_at',
            field=models.DateTimeField(help_text='When the charge was created', verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='description',
            field=models.CharField(help_text='A description of what the charge was for', max_length=255, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='organization',
            field=models.ForeignKey(help_text='The organization charged', on_delete=django.db.models.deletion.PROTECT, related_name='charges', to='organizations.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='accepted_at',
            field=models.DateTimeField(blank=True, help_text='When this invitation was accepted.  NULL signifies it has not been accepted yet', null=True, verbose_name='accepted at'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='created_at',
            field=squarelet.core.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, help_text='When this invitation was created', verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='email',
            field=models.EmailField(help_text='The email address to send this invitation to', max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='organization',
            field=models.ForeignKey(help_text='The organization this invitation is for', on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='organizations.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='rejected_at',
            field=models.DateTimeField(blank=True, help_text='When this invitation was rejected.  NULL signifies it has not been rejected yet', null=True, verbose_name='rejected at'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='user',
            field=models.ForeignKey(blank=True, help_text='The user this invitation is for.  Used if a user requested an invitation directly as opposed to an admin inviting them via email.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='invitations', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='This UUID serves as a secret token for this invitation in URLs', verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='organizations.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='avatar',
            field=sorl.thumbnail.fields.ImageField(blank=True, help_text='An image to represent the organization', upload_to='org_avatars', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='created_at',
            field=squarelet.core.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, help_text='When this organization was created', verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='customer_id',
            field=models.CharField(blank=True, help_text="The organization's corresponding ID on stripe", max_length=255, null=True, unique=True, verbose_name='customer id'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='max_users',
            field=models.IntegerField(default=5, help_text='The maximum number of users in this organization', verbose_name='maximum users'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(help_text='The name of the organization', max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='next_plan',
            field=models.ForeignKey(help_text='The pending plan to be updated to on the next billing cycle - used when downgrading a plan to let the organization finish out a subscription is paid for', on_delete=django.db.models.deletion.PROTECT, related_name='pending_organizations', to='organizations.Plan', verbose_name='next plan'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='payment_failed',
            field=models.BooleanField(default=False, help_text='A payment for this organization has failed - they should update their payment information', verbose_name='payment failed'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='plan',
            field=models.ForeignKey(help_text='The current plan this organization is subscribed to', on_delete=django.db.models.deletion.PROTECT, related_name='organizations', to='organizations.Plan', verbose_name='plan'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='private',
            field=models.BooleanField(default=False, help_text="This organization's information and membership is not made public", verbose_name='private organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, help_text='A unique slug for use in URLs', populate_from='name', unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='subscription_id',
            field=models.CharField(blank=True, help_text="The organization's corresponding subscription ID on stripe", max_length=255, null=True, unique=True, verbose_name='subscription id'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='updated_at',
            field=squarelet.core.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, help_text='When this organization was last updated', verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(help_text="The user's in this organization", related_name='organizations', through='organizations.Membership', to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Uniquely identify the organization across services', unique=True, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='organizationchangelog',
            name='created_at',
            field=squarelet.core.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, help_text='When the organization was changed', verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='organizationchangelog',
            name='from_max_users',
            field=models.IntegerField(blank=True, help_text="The organization's max_users before the change occurred", null=True, verbose_name='maximum users'),
        ),
        migrations.AlterField(
            model_name='organizationchangelog',
            name='from_next_plan',
            field=models.ForeignKey(blank=True, help_text="The organization's next_plan before the change occurred", null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='organizations.Plan', verbose_name='from next plan'),
        ),
        migrations.AlterField(
            model_name='organizationchangelog',
            name='from_plan',
            field=models.ForeignKey(blank=True, help_text="The organization's plan before the change occurred", null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='organizations.Plan', verbose_name='from plan'),
        ),
        migrations.AlterField(
            model_name='organizationchangelog',
            name='organization',
            field=models.ForeignKey(help_text='The organization which changed', on_delete=django.db.models.deletion.CASCADE, related_name='change_logs', to='organizations.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='organizationchangelog',
            name='reason',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Created'), (1, 'Updated'), (2, 'Payment failed')], help_text='Which category of change occurred', verbose_name='reason'),
        ),
        migrations.AlterField(
            model_name='organizationchangelog',
            name='to_max_users',
            field=models.IntegerField(help_text="The organization's max_users after the change occurred", verbose_name='maximum users'),
        ),
        migrations.AlterField(
            model_name='organizationchangelog',
            name='to_next_plan',
            field=models.ForeignKey(help_text="The organization's plan after the change occurred", on_delete=django.db.models.deletion.PROTECT, related_name='+', to='organizations.Plan', verbose_name='to next plan'),
        ),
        migrations.AlterField(
            model_name='organizationchangelog',
            name='to_plan',
            field=models.ForeignKey(help_text="The organization's plan after the change occurred", on_delete=django.db.models.deletion.PROTECT, related_name='+', to='organizations.Plan', verbose_name='to plan'),
        ),
        migrations.AlterField(
            model_name='organizationchangelog',
            name='user',
            field=models.ForeignKey(blank=True, help_text='The user who changed the organization', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='change_logs', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='base_price',
            field=models.PositiveSmallIntegerField(default=0, help_text='The price per month for this plan with the minimum number of users', verbose_name='base price'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='feature_level',
            field=models.PositiveSmallIntegerField(default=0, help_text='Specifies the level of premium features this plan grants', verbose_name='feature level'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='minimum_users',
            field=models.PositiveSmallIntegerField(default=1, help_text='The minimum number of users allowed on this plan', verbose_name='minimum users'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(help_text="The plan's name", max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='price_per_user',
            field=models.PositiveSmallIntegerField(default=0, help_text='The additional cost per month per user over the minimum', verbose_name='price per user'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='private_organizations',
            field=models.ManyToManyField(help_text='For private plans, organizations which should have access to this plan', related_name='private_plans', to='organizations.Organization', verbose_name='private organizations'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='public',
            field=models.BooleanField(default=False, help_text='Is this plan available for anybody to sign up for?', verbose_name='public'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, help_text='A uinique slug to identify the plan', populate_from='name', unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='receiptemail',
            name='email',
            field=django.contrib.postgres.fields.citext.CIEmailField(help_text='The email address to send the receipt to', max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='receiptemail',
            name='failed',
            field=models.BooleanField(default=False, help_text='Has sending to this email address failed?', verbose_name='failed'),
        ),
        migrations.AlterField(
            model_name='receiptemail',
            name='organization',
            field=models.ForeignKey(help_text='The organization this receipt email corresponds to', on_delete=django.db.models.deletion.CASCADE, related_name='receipt_emails', to='organizations.Organization', verbose_name='organization'),
        ),
    ]