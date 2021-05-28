#local
from django.urls import path

#app
from . import views

app_name = 'comments_app'

urlpatterns = [
    path('create-comment/', views.CreateComment.as_view(), name = 'create_comment'),
    path('commet-collection/<candidate_id>/<category_comment_id>/', views.CommentsPagination.as_view(), name = 'commet_collection'),
]

