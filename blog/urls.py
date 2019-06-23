from django.conf.urls import url
from .views import archive, single

urlpatterns = [
    url(r'^$', archive, name='blog_archive'),
    url(r'^(?P<pk>\d+)/$', single, name='blog_single')
]
