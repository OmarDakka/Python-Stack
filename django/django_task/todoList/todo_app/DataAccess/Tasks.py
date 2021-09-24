from login_app.models import users
from todo_app.models import Category, Task

##Added the CRUD methods for the Task class in order to get results, create new task, edit task and delete task
def get_all_tasks():
    results = Task.objects.all()
    return results


def get_task(id):
    result = Task.objects.get(id=id)
    return result


def create_task(title, user_id, category_id, description, duedate):
    user = users.objects.get(id=user_id)
    category = Category.objects.get(id = category_id)
    result = Task.objects.create(title=title, created_by=user,
                                 category=category, description=description, duedate=duedate)
    return result


def update_task(id, title, user_id, category_id ,description, duedate):
    task = Task.objects.get(id=id)
    user = users.objects.get(id=user_id)
    category = Category.objects.get(id = category_id)
    task.title = title
    task.description = description
    task.duedate = duedate
    task.created_by = user
    task.category = category
    task.save()
    return task


def delete_task(id):
    task = Task.objects.get(id=id)
    return task.delete()
