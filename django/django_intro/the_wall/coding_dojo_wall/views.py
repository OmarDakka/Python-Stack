from login.models import users
from coding_dojo_wall.models import post_creation,comment_creation
from django.shortcuts import redirect, render
from .models import  posts,comments


def index(request):
    user = request.session['first_name']+" "+request.session['last_name']
    user_id = request.session['id']
    creation = posts.objects.all().order_by("-created_at")
    replies = comments.objects.all().order_by("-created_at")
    context = {
        "user" : user,
        "user_id" : user_id,
        "creation" : creation,
        "replies" : replies
    }
    return render(request,"wall.html",context)

def create_post(request):
    print(request.session['id'])
    post_creation(request.POST["postMessage"], users.objects.get(id = request.session['id']))
    return redirect('/wall')

def create_comment(request,post_id):
    comment_creation(request.POST["postComment"],users.objects.get(id = request.session['id']), post_id)
    return redirect('/wall')

# def delete_post(request):
#     if request.session['id'] == users.posts.id:
#         post_deletion()
#     return redirect('/wall')
