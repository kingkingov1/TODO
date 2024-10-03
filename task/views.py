from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from task.forms import TaskForm
from task.models import Task


def task_view(request, sms, code, css_class):
    if code == 'TODO':
        tasks = Task.todo.all()
    elif code == 'DONE':
        tasks = Task.done.all()
    elif code == 'DELETE':
        tasks = Task.delete.all()
    elif code == 'DONE & DELETE':
        tasks = Task.done_delete.all()
    else:
        tasks = Task.objects.none()

    form = TaskForm()
    paginator = Paginator(tasks, 7)
    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    context = {
        'tasks': tasks,
        'form': form,
        'sms': sms,
        'task_code': code,
        'class': css_class,
        'todo_count': Task.todo.all().count(),
        'done_count': Task.done.all().count(),
        'deleted_count': Task.delete.all().count(),
        'done_delete_count': Task.done_delete.all().count(),
        # 'search': code.lower()
    }

    return render(request, 'task/home.html', context)


def home_view(request):
    return task_view(request, 'Bajarilmagan', 'TODO', 'warning')


def task_done_view(request):
    return task_view(request, 'Bajarilgan', 'DONE', 'success')


def task_delete_view(request):
    return task_view(request, 'O\'chirilgan', 'DELETE', 'danger')


def done_delete_task_view(request):
    return task_view(request, 'Bajarilgan va O`chirilgan', 'DONE & DELETE', 'dark')


def search(request):
    q = request.POST.get('search', '') if request.method == 'POST' else request.GET.get('search', '')

    if not q.strip():
        tasks = Task.objects.none()
    else:
        tasks = Task.objects.filter(title__icontains=q)

    tasks_count = tasks.count()
    paginator = Paginator(tasks, 7)
    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    if tasks_count > 0:
        messages.success(request, f"{q} {'haqida' if q else ''} {tasks_count} ta ma'lumot topildi!")
    else:
        messages.error(request, f"{q} haqida ma'lumot topilmadi!")

    context = {
        'tasks': tasks,
        'form': TaskForm(),
        'class': 'dark',
        'sms': 'Qidirilgan',
        'todo_count': Task.todo.all().count(),
        'done_count': Task.done.all().count(),
        'deleted_count': Task.delete.all().count(),
        'done_delete_count': Task.done_delete.all().count(),
        'search': q
    }

    return render(request, 'task/home.html', context)


def custom_redirect(task):
    if task.is_done and task.is_delete:
        return redirect('done-delete-task-view')
    elif task.is_delete:
        return redirect('task-delete-view')
    elif task.is_done:
        return redirect('task-done-view')
    else:
        return redirect('home-view')


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f"{task.title} Topshiriq muvaffaqqiyatli yaratildi!")
            # custom redirect
            return custom_redirect(task)


def edit_task(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = Task.objects.get(pk=task_id)
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.is_done = request.POST.get('done', 'off') == 'on'
        task.is_delete = request.POST.get('delete', 'off') == 'on'
        task.save()
        messages.success(request, f"{task.title} topshiriq o'zgartirildi!")
        # custom redirect
        return custom_redirect(task)


def done_task(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = Task.objects.get(pk=task_id)
        task.done = True
        task.save()
        messages.success(request, f"{task.title} Topshiriq muvaffaqqiyatli bajarildi!")
        # custom redirect
        return custom_redirect(task)


def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = Task.objects.get(pk=task_id)
        task.is_delete = True
        task.save()
        messages.success(request, f"{task.title} фвцTopshiriq muvaffaqqiyatli o'chirildi!")
        # custom redirect
        return custom_redirect(task)




