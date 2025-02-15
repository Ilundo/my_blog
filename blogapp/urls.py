from django.urls import path
from .views import posts_by_author, posts_list

urlpatterns = [
    path("post/list/", posts_list),
    path("author/posts/<int:author_id>",posts_by_author)
]
