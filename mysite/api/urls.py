from django.urls import path
from polls import views_restframework

urlpatterns = [
    path('items/', views_restframework.hello_world, name='hello_world'),
]