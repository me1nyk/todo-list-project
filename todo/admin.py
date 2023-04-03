from django.contrib import admin

from todo.models import Tag, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "deadline", "is_done"]
    list_filter = ["is_done"]
    search_fields = ["tags"]


admin.site.register(Tag)
admin.site.register(Task, TaskAdmin)

