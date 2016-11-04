from django.conf.urls import url
from django.contrib import admin

from events.views import EventListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', EventListView.as_view(), name='event-list'),
]
