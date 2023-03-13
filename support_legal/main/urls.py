from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post_list", views.post_list, name="post_list"),
    path("post_detail/<post_id>", views.post_detail, name="post_detail"),
    path("create-post", views.create_post, name="create_post"),
    path("post_update/<post_id>", views.update_post, name="update_post"),
    path("sign-up", views.sign_up, name="sign_up"),
]