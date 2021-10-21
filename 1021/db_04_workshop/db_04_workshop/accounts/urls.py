from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<username>/',views.profile,name='profile'),               # 프로파일 함수는 항상 맨 마지막 순서여야만 함 
    path('follow/<int:user_pk>', views.follow,name='follow'),
]
