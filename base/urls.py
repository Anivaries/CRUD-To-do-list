from .views import ToDoListView, ToDoDetailView, create_new, delete, update
from django.urls import path
# ToDoCreateView, ToDoDeleteView ToDoUpdateView,
urlpatterns = [
    path('', ToDoListView.as_view(), name='todo-list'),
    path('task/<int:pk>/', ToDoDetailView.as_view(), name='task-detail'),
    # path('create/', ToDoCreateView.as_view(), name='todo-form'),
    # path('task/<int:pk>/update', ToDoUpdateView.as_view(), name='task-update'),
    path('create/', create_new, name='create-task'),
    path('task/<int:pk>/delete', delete, name='task-delete'),
    path('task/<int:pk>/update', update, name='task-update'),

]
