from django.urls import path

from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    task_remove_or_assign
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="index-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="index-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="index-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("<int:pk>/assign/", task_remove_or_assign, name="task-remove-or-assign"),
]

app_name = "todo"
