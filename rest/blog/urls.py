from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, CommentViewSet

router = DefaultRouter()
router.register('blog-posts', BlogPostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#to see the list of post and add a post you can use: http://127.0.0.1:8000/blog-post
#to view a detailed post and update it you can use :http://127.0.0.1:8000/blog-post/<id>
#same goes for comments -> to retrive,add :http://127.0.0.1:8000/comments
#to update,delete -> http://127.0.0.1:8000/comments/<id>