from django.conf.urls import url
from .views import add, view, delete, adjust

urlpatterns = [
    url(r'^$', view, name='cart'),
    url(r'^add/(?P<feature_id>\d+)/$', add, name='cart_add'),
    url(r'^adjust/(?P<action>[-\w]+)/(?P<feature_id>\d+)/$', adjust, name='cart_adjust'),
    url(r'^delete/(?P<feature_id>\d+)/$', delete, name='cart_delete')
]
