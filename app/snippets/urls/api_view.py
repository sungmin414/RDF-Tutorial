from rest_framework.urlpatterns import format_suffix_patterns

from ..views import api_view as views
from django.urls import path

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippets-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippets-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)