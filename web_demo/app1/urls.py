
from django.urls import path
from app1 import views as app1_views
urlpatterns = [
    path('article/<int:year>',app1_views.article),
    path('get_name',app1_views.get_name)
]
