from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ToDo
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .forms import CreateTaskForm, UpdateTaskForm


class ToDoListView(ListView):
    model = ToDo
    context_name = 'todolist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo"] = ToDo.objects.all()
        return context


class ToDoDetailView(DetailView):
    model = ToDo

    def get_queryset(self):
        return super().get_queryset()

# class ToDoUpdateView(UpdateView):
#     model = ToDo
#     template_name = 'update.html'
#     fields = ['completed']


# class ToDoCreateView(CreateView):
#     model = ToDo
#     fields = ['title', 'description']


# class ToDoDeleteView(DeleteView):
#     model = ToDo
#     template_name = 'delete.html'
#     success_url = reverse_lazy('todo-list')


def create_new(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
        else:
            return HttpResponse('404')
    else:
        form = CreateTaskForm()
    return render(request, 'todo_form.html', {"form": form})


def delete(request, pk):
    task = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('todo-list')
    else:
        return render(request, 'delete.html')


def update(request, pk):
    instance = get_object_or_404(ToDo, pk=pk)
    form = UpdateTaskForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('todo-list')
    return render(request, 'update.html', {"form": form})
