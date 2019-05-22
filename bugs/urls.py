from django.conf.urls import url, include
from .views import archive, single, add_or_edit, vote, delete

urlpatterns = [
    url(r'^$', archive, name='bug_archive'),
    url(r'^(?P<pk>\d+)/$', single, name='bug_single'),
    url(r'^vote/(?P<pk>\d+)/$', vote, name='bug_vote'),
    url(r'^new/$', add_or_edit, name='bug_new'),
    url(r'^edit/(?P<pk>\d+)/$', add_or_edit, name='bug_edit'),
    url(r'^delete/(?P<pk>\d+)/$', delete, name='bug_delete'),
]