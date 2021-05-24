from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.books),
    path('add_book',views.add_book),
    path('authors',views.authors),
    path('add_author',views.add_author),
    path('view_book/<int:book_id>',views.view_book),
    path('add_author_to_book/<int:book_id>', views.add_author_to_book),
    path('view_author/<int:author_id>', views.view_author),
    path('add_book_to_author/<int:author_id>', views.add_book_to_author),
    path('go_to_authors', views.go_to_authors),
    path('go_to_books', views.go_to_books)
]
