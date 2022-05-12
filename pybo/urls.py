from django.urls import path

from . import views

app_name = 'pybo'
# urlpatterns = [
#     path('', views.index),
#     path('<int:question_id>/', views.detail),
# ]

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:pk>/', views.DetailView.as_view()),
]