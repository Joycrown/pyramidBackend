from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.query_regex, name='query-regex'),
]
