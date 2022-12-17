from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
    path('', views.PostListView.as_view(),name='post_list'),
    path('<int:pk>/',views.PostDetailView.as_view(), name='post_details'),
    # path('create/',views.PostCreateView.as_view(),name='create'),
    path('create', views.CreatePostView.as_view(), name='create'),
    path('createcom', views.CommentCreateView.as_view(), name='createcom'),
    # path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    # path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete'),
]
