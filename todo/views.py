from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_confirm_delete.html"


def task_remove_or_assign(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return redirect('todo:index')
