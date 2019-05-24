from django.conf.urls import url, include
from .views import archive, single, add, edit, vote, delete

urlpatterns = [
    url(r'^$', archive, name='bug_archive'),
    url(r'^(?P<pk>\d+)/$', single, name='bug_single'),
    url(r'^vote/(?P<pk>\d+)/$', vote, name='bug_vote'),
    url(r'^new/$', add, name='bug_new'),
    url(r'^edit/(?P<pk>\d+)/$', edit, name='bug_edit'),
    url(r'^delete/(?P<pk>\d+)/$', delete, name='bug_delete'),
]
