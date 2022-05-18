from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]

# for generic view
# urlpatterns = [
#     path('', views.IndexView.as_view()),
#     path('<int:pk>/', views.DetailView.as_view()),
# ]