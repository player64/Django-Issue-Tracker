from django.conf.urls import url
from .views import add, view, delete

urlpatterns = [
    url(r'^$', view, name='cart'),
    url(r'^add/(?P<feature_id>\d+)/$', add),
    url(r'^delete/(?P<feature_id>\d+)/$', delete)
]
