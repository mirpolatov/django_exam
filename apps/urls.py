from django.urls import path

from apps.views import register, main, CustomLoginView, userfunc, deletefunc, users_list

urlpatterns = [
    path('', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('update/<int:pk>', userfunc, name='update'),
     path('delete/<int:pk>', deletefunc, name='delete'),

    path('main/', users_list, name='main')
]
