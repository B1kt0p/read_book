from django.urls import path, re_path

from blog import views



urlpatterns = [
    re_path(r'^(?:(?P<id>\d+)/)?$', views.index, name='index'),
    path('good/<int:id>/', views.good, name='good'),

]

