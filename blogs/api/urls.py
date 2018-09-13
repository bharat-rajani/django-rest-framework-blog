from django.urls import path, re_path, include
from .views import *


urlpatterns = [
    path('',BlogPostAPIView.as_view(),name='post-create'),
    re_path(r'^(?P<pk>\d+)$',BlogPostRudView.as_view(),name='post-rud'),
]