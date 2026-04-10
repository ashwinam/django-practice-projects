from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.SnippetListView.as_view(), name="snippet-list"),
    path("<int:pk>/", views.SnippetDetailView.as_view(), name="snippet-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)