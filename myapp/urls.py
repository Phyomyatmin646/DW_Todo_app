from django.urls import path
from.import views
urlpatterns=[
    path('',views.Todolist, name="Todolist"),
    path('create',views.todocreate, name="Todocreate"),
    path('detail/<uuid:pk>/',views.tododetail,name="Tododetail"),
    path('update/<uuid:pk>/',views.todoupdate,name="Todoupdate"),
    path('delete/<uuid:pk>/',views.tododelete,name="Tododelete"),
]