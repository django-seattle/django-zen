from django.conf.urls import patterns, url
from apps.foundation.views import FoundationTemplateView

urlpatterns = patterns('',
    url(r'^$', FoundationTemplateView.as_view()),
)
