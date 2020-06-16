from django.urls import path
from . import views
from .views import (

    HomeView,
    PostDetailView,
    like

)
app_name = 'blog'

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('<slug>/', PostDetailView.as_view(), name='detail'),
    path('like/<slug>/', views.like, name='like')
]
