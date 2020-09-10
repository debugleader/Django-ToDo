from django.urls import path
from .views import index, addToDo, completeToDo, undoToDo, deleteCompleted, deleteAdd

urlpatterns = [
    path('', index, name = 'index'),
    path('add', addToDo, name = 'add'),
    path('complete/<todo_id>', completeToDo, name = 'complete'),
    path('undo/<todo_id>', undoToDo, name = 'undo'),
    path('deletecomplete', deleteCompleted, name = 'deletecomplete'),
    path('deleteadd', deleteAdd, name = 'deleteadd')
]