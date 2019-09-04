from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('', views.base, name='base'),
    path('comment/', views.comment, name='comment'),
    path('comment_index/', views.comment_index, name='comment_index'),

    path('upload_image/', views.upload_image, name='upload_image'),

    path('moviereview/', views.review, name='review'),
    path('review_result/', views.review_result, name='review_result'),

    path('article/create', views.article_create),
    path('article/', views.ArticleList, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/edit', views.article_update, name='article_update'),
    path('article/<int:pk>/delete', views.article_delete, name='article_delete'),

    path('project_signin', views.project_signin, name='project_signin'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
