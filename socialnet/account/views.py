from __future__ import unicode_literals

from django.views.generic import ListView

from account.models import User


class UserListView(ListView):
    template_name = 'account/user_list.html'
    queryset = User.objects.all()
    context_object_name = 'users'
