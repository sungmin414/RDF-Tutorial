from django.urls import path, include
from .. import views

app_name='snippets'

urlpatterns = [
    path('django_view/', include('snippets.urls.django_view')),
]