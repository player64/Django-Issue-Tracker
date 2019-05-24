from django.conf.urls import url, include
from .views import archive, single, add, edit, delete

urlpatterns = [
    url(r'^$', archive, name='feature_archive'),
    url(r'^(?P<pk>\d+)/$', single, name='feature_single'),
    url(r'^new/$', add, name='feature_new'),
    url(r'^edit/(?P<pk>\d+)/$', edit, name='bug_edit'),
    url(r'^delete/(?P<pk>\d+)/$', delete, name='bug_delete'),
]