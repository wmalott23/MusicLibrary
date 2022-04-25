from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_library_list),
    path('<int:pk>/', views.music_library_details),
    path('liked/<int:pk>/', views.music_library_like),
    path('disliked/<int:pk>/', views.music_library_dislike),
]