from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.http import Http404
from django.views.generic import ListView, DetailView

from account.models import User


class UserListView(ListView):
    template_name = 'account/user_list.html'
    queryset = User.objects.all()
    context_object_name = 'users'


class UserDetailsView(DetailView):
    template_name = 'account/user_detail.html'
    model = User
    context_object_name = 'user'