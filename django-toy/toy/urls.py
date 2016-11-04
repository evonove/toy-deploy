from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.cache import cache_control

from events.views import EventListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', cache_control(must_revalidate=True, max_age=60)(EventListView.as_view()), name='event-list'),
]
