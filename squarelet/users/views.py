# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

# Local
from .models import User
from .tasks import push_update_user


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User

    def get_form_class(self):
        """Include username in form if the user hasn't changed their username yet"""
        fields = ["name", "avatar"]
        if self.object.can_change_username:
            self.fields = ["username"] + fields
        else:
            self.fields = fields
        return super().get_form_class()

    def form_valid(self, form):
        with transaction.atomic():
            self.object = form.save()
            if self.request.user.username != self.object.username:
                self.object.can_change_username = False
                self.object.save()
            transaction.on_commit(lambda: push_update_user.delay(self.object.pk))
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.object.username})

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)


class UserListView(LoginRequiredMixin, ListView):
    model = User
