from login_app.models import users
from todo_app.models import Category

##Added the CRUD methods for the Category class in order to get results, create new category, edit category and delete category
def get_all_categories():
    results = Category.objects.all()
    return results

def get_category(id):
    result = Category.objects.get(id = id)
    return result

def create_category(title , user_id):
    user = users.objects.get(id = user_id)
    result = Category.objects.create(title = title, created_by = user)
    return result

def update_category(id, title , user_id):
    category = Category.objects.get(id = id)
    user = users.objects.get(id = user_id)
    category.title = title
    category.created_by = user
    category.save()
    return category

def delete_category(id):
    category = Category.objects.get(id = id)
    return category.delete()

