from django.conf.urls import url

from .views import SiteListView, SiteDetailView

urlpatterns = [
    url(r'^$', SiteListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', SiteDetailView.as_view(), name='detail'),
]
