from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Task  # Make sure this line is included
from rest_framework.views import APIView

from rest_framework.response import Response

from .serializers import TaskSerializer

from django.views.decorators.csrf import csrf_exempt

class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



from django.shortcuts import render, redirect
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(title=title)  # Save new task

        # HTMX Request
        if request.headers.get('HX-Request'):
            tasks = Task.objects.all()  # Fetch all tasks
            html = render_to_string('todo/task_items.html', {'tasks': tasks})
            return HttpResponse(html)

        # Non-HTMX Fallback
        return redirect('/')

    # Fallback for GET request
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})



def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle the completed status
    task.save()

    # HTMX Request: Return updated task list dynamically
    if request.headers.get('HX-Request'):
        tasks = Task.objects.all()
        html = render_to_string('todo/task_items.html', {'tasks': tasks})
        return HttpResponse(html)

    # Non-HTMX Fallback
    return redirect('/')



def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'todo/task_list.html', {'tasks': tasks})


def delete_task(request, task_id):
    # Fetch the task, return 404 if not found
    task = get_object_or_404(Task, id=task_id)
    task.delete()  # Delete the task

    # If it's an HTMX request, return updated task list
    if request.headers.get('HX-Request'):
        tasks = Task.objects.all()
        html = render_to_string('todo/task_items.html', {'tasks': tasks})
        return HttpResponse(html)

    # Fallback for non-HTMX requests (redirect)
    return redirect('task_list')