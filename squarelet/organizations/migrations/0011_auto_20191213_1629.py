# Generated by Django 2.1.7 on 2019-12-13 21:29

# Django
from django.db import migrations

# Standard Library
from datetime import date

ENTITLEMENTS = [
    {
        "name": "Professional",
        "description": "An individual account will receive 20 requests per "
        "month, the ability to embargo requests, and a discounted bulk "
        "rate on additional requests.",
        "plans": ["professional", "professional-pre-paid", "proxy"],
    },
    {
        "name": "Organization",
        "description": "A organization account will receive 50 requests "
        "per month, the ability to permanantly embargo requests, and a "
        "discounted bulk rate on additional requests.",
        "plans": ["organization", "organization-annual"],
    },
    {
        "name": "Admin",
        "description": "Free requests for staff only",
        "plans": ["admin"],
    },
    {
        "name": "Beta",
        "description": "5 requests per month for our earliest users",
        "plans": ["beta"],
    },
    {
        "name": "Custom CRP",
        "description": "Custom entitlement for CRP",
        "plans": ["custom-crp"],
    },
    {"name": "WBRC", "description": "Custom entitlement for WBRC", "plans": ["wbrc"]},
    {
        "name": "Education Grant",
        "description": "An organization account with more users, intended "
        "only for educational partners",
        "plans": ["education-grant"],
    },
]


def create_subscriptions(apps, schema_editor):
    """Switch from single plan to multi plan database model"""
    Organization = apps.get_model("organizations", "Organization")
    Subscription = apps.get_model("organizations", "Subscription")

    for organization in Organization.objects.exclude(plan__slug="free"):
        # ensure any pending organization changes are simple cancels
        assert (
            organization.plan == organization.next_plan
            or organization.next_plan.slug == "free"
        )
        Subscription.objects.create(
            organization=organization,
            plan=organization.plan,
            subscription_id=organization.subscription_id,
            update_on=organization.update_on
            if organization.update_on is not None
            else date.today(),
            cancelled=organization.next_plan.slug == "free",
        )


def create_entitlements(apps, schema_editor):
    """Create entitlements based on plans"""
    Plan = apps.get_model("organizations", "Plan")
    Entitlement = apps.get_model("organizations", "Entitlement")
    Client = apps.get_model("oidc_provider", "Client")

    muckrock_client = Client.objects.get(name__startswith="MuckRock")

    for entitlement_data in ENTITLEMENTS:
        entitlement = Entitlement.objects.create(
            name=entitlement_data["name"],
            description=entitlement_data["description"],
            client=muckrock_client,
        )
        entitlement.plans.set(Plan.objects.filter(slug__in=entitlement_data["plans"]))


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0010_auto_20191213_1627"),
        ("oidc_provider", "0026_client_multiple_response_types"),
    ]

    operations = [
        migrations.RunPython(create_subscriptions, migrations.RunPython.noop),
        migrations.RunPython(create_entitlements, migrations.RunPython.noop),
    ]