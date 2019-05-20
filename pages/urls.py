from django.conf.urls import url
from .views import home_page, about_page, stats_page

urlpatterns = [
    url(r'^$', home_page, name='index'),
    url(r'^about-us/$', about_page, name='page_about'),
    url(r'^stats/$', stats_page, name='page_stats')
]
