from django.urls import path
from . import views
from .views import create_post
from .views import PostListView

app_name = 'kouryakusaito'

#URLパターンを登録する
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'kouryaku-detail/<int:pk>/',
        views.KouryakuDetail.as_view(),
        name='kouryaku_detail'
        ),
        
    path(
        'character/',
        views.CharacterView.as_view(),
        name='character'
    ),

        path(
        'enemy/',
        views.EnemyView.as_view(),
        name='enemy'
    ),

    path(
        'item/',
        views.ItemView.as_view(),
        name='item'
    ),

    path(
        'keijiban/',
        views.KeijibanView.as_view(),
        name='keijiban'
    ),

    path(
        'contact/',
        views.ContactView.as_view(),
        name='contact'
    ),

    path(
        'kouryaku-detail/<int:pk>/',
        views.KouryakuDetail.as_view(),
        name='kouryaku_detail'
    ),

    path(
        'gamesystem/',
        views.GamesystemView.as_view(),
        name='gamesystem'
    ),

    path(
        'create-post/',
        views.create_post,
        name='create_post'
    ),

    path(
        'keijiban/',
        PostListView.as_view(),
        name='keijiban'
    ),

    path(
        'delete-post/<int:pk>/', 
        views.delete_post, 
        name='delete_post'
    ),

    path(
        'category/<str:category>/', 
        views.keijiban_by_category, 
        name='keijiban_by_category'),

    
]
    