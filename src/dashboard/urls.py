from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("delete/<int:task_id>", views.delete),
    path("update/<int:task_id>", views.update)
]
