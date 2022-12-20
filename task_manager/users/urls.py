from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.UserIndexView.as_view(), name='index'),
    path('create/', views.UserFormCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', views.UserFormUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
]
