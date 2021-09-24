from todo_app.DataAccess.Tasks import create_task, delete_task, get_all_tasks, get_task, update_task
from django.http.response import JsonResponse
from django.views.generic.base import View
from todo_app.DataAccess.Categories import create_category, delete_category, get_all_categories, get_category, update_category
from django.shortcuts import render
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#This defintion will render the Homepage that we land on upon successfull login.
#The defintion also puts the user's name and id in context in able to be used in the html to be able to show them.
def index(request):
    user = request.session['first_name'] + " " + request.session['last_name']
    user_id = request.session['id']
    context = {
        "user": user,
        "user_id": user_id
    }
    return render(request, "index.html", context)


#First class for the APIs of the category model, includes all the functions of the requests: post, get, put and delete.
#Each function return a JsonResponse data to be able to use and view in the front-end side
@method_decorator(csrf_exempt, name='dispatch')
class category_api(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        result = create_category(
            data.get('title'), data.get('user_id'))
        return JsonResponse(result.to_json(), status=201)

    def get(self, request, id=0):
        if (id == 0):
            categories = get_all_categories()

            category_data = []

            for category in categories:
                category_data.append(category.to_json())

            data = {
                'items': category_data
            }

            return JsonResponse(data)
        else:
            category = get_category(id)
            return JsonResponse(category.to_json())

    def put(self, request, id):
        data = json.loads(request.body.decode("utf-8"))
        category = update_category(id,data.get('title'), data.get('user_id'))
        return JsonResponse(category.to_json(), status=200)

    def delete(self, request, id):
        delete_category(id)
        return JsonResponse({}, status=204)

#Second Task that has all the Task model APIs that also include requests that are post, get, put and delete.
#The functions also return a JSON response in order to use the data properly and easily.
@method_decorator(csrf_exempt, name='dispatch')
class task_api(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        result = create_task(data.get('title'), data.get('user_id'), data.get('category_id'), data.get('description'), data.get('duedate'))
        return JsonResponse(result.to_json(), status=201)

    def get(self, request, id=0):
        if (id == 0):
            tasks = get_all_tasks()

            task_data = []

            for task in tasks:
                task_data.append(task.to_json())
            
            data = {
                'tasks' : task_data
            }

            return JsonResponse(data)
        else:
            task = get_task(id)
            return JsonResponse(task.to_json())
    
    def put(self, request, id):
        data = json.loads(request.body.decode("utf-8"))
        task = update_task(id, data.get('title'), data.get('user_id'), data.get('category_id'), data.get('description'), data.get('duedate'))
        return JsonResponse(task.to_json(), status=200)
    
    def delete(self, request, id):
        delete_task(id)
        return JsonResponse({}, status=204)
    