from django.shortcuts import render,redirect,get_object_or_404
from .models import TodoModel
# Create your views here.
def Todolist(request):
    todo=TodoModel.objects.all()
    context={
        'todo':todo
    }
    return render(request,'index.html',context)
# create function
def todocreate(request):
    if request.method == 'POST':
        title= request.POST.get('title')
        description= request.POST.get('description')
        completed= request.POST.get('completed')=='on'
        TodoModel.objects.create(
            title=title,
            description=description,
            completed=completed,
        )
        return redirect('Todolist')
    return render(request,'todo_form.html')
#Detail Function
def tododetail(request,pk):
        todo = get_object_or_404(TodoModel,pk=pk)
        return render(request, 'todo_detail.html',{'todo':todo})
#Update Function
def todoupdate(request, pk):
        todo = get_object_or_404(TodoModel, pk=pk)
        if request.method == 'POST':
            todo.title=request.POST.get('title')
            todo.description= request.POST.get('description')
            todo.completed=request.POST.get('completed') == 'on'
            todo.save()
            return redirect('Todolist')
        return render (request, 'todo_form.html', {'todo':todo})
#Delete Function
def tododelete(request, pk):
     todo = get_object_or_404(TodoModel,pk=pk)
     if request.method == 'POST':
          todo.delete()
          return redirect('Todolist')
     return render(request, 'index.html',{'todo':todo})