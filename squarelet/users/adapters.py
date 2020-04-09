# Django
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import is_safe_url

# Third Party
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from furl import furl

# Squarelet
from squarelet.core.mail import Email


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def render_mail(self, template_prefix, email, context):
        """
        Renders an e-mail to `email`.  `template_prefix` identifies the
        e-mail that is to be sent, e.g. "account/email/email_confirmation"
        """

        # we need to prefix the subject template here because it's getting
        # rendered here; the actual email body template is rendered in the
        # Email class, which also fixes the template prefix
        #
        # if we were to add "presspass/" to the template_prefix here, the message
        # body template would become "presspass/presspass/etc/etc.html" in Email()
        subject_template = f"{template_prefix}_subject.txt"
        source = context.get("source") or "muckrock"
        if source == "presspass":
            subject_template = "presspass/" + subject_template

        subject = render_to_string(subject_template, context)
        # remove superfluous line breaks
        subject = " ".join(subject.splitlines()).strip()

        return Email(
            subject=subject,
            template=f"{template_prefix}_message.html",
            to=[email],
            extra_context=context,
            source=source,
        )

    def is_safe_url(self, url):
        allowed_hosts = [
            furl(settings.SQUARELET_URL).host,
            furl(settings.MUCKROCK_URL).host,
            furl(settings.FOIAMACHINE_URL).host,
            furl(settings.DOCCLOUD_URL).host,
            furl(settings.PRESSPASS_URL).host,
        ]
        return is_safe_url(url, allowed_hosts=allowed_hosts)

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = get_current_site(request)

        activate_url = self.get_email_confirmation_url(request, emailconfirmation)

        source_site = request.get_host()
        squarelet_source = "muckrock"
        if source_site == furl(settings.PRESSPASS_URL).host:
            squarelet_source = "presspass"

        ctx = {
            "user": emailconfirmation.email_address.user,
            "activate_url": activate_url,
            "current_site": current_site,
            "key": emailconfirmation.key,
            "source": squarelet_source,
        }
        if signup:
            email_template = "account/email/email_confirmation_signup"
        else:
            email_template = "account/email/email_confirmation"

        self.send_mail(email_template, emailconfirmation.email_address.email, ctx)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
