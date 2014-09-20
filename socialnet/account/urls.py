from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from account.views import UserListView, UserDetailsView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socialnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', UserListView.as_view(), name='user_list'),
    url(r'^(?P<pk>[\w]+)/$', UserDetailsView.as_view(), name='user_detail'),
)
