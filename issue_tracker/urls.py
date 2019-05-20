"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from .settings import MEDIA_ROOT, WEBPACK_COMPILED_ASSETS
from accounts import urls as urls_accounts
from pages import urls as pages_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^compiled-static/webpack-bundle/(?P<path>.*)$', static.serve, {'document_root': WEBPACK_COMPILED_ASSETS}),
    url(r'^', include(pages_urls), name='pages'),
    url(r'^accounts/', include(urls_accounts)),
]
