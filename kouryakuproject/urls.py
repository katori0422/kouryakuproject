from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

#　プロジェクトのURLパターンを登録するリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスがadmin/にマッチングした場合
    # admin.site.urlsを呼び出し、Django管理サイトを表示する
    path('admin/', admin.site.urls),

    #　http(s)://ホスト名/へのアクセスはkouryakusaitoの
    #　URLconf(urls.py)を呼び出す
    path('', include('kouryakusaito.urls')),

    path('', include('accounts.urls')),

    # パスワードリセットのためのURLパターン
    # PasswordResetConfirmViewがプロジェクトのurls.pyを参照するのでここに記載
    # パスワードリセット申し込みページ
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
           template_name = "password_reset.html"),
         name ='password_reset'),
    
    # メール送信完了ページ
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
           template_name = "password_reset_sent.html"),
         name ='password_reset_done'),
    
    # パスワードリセットページ
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
           template_name = "password_reset_form.html"),
         name ='password_reset_confirm'),
    
    # パスワードリセット完了ページ
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
           template_name = "password_reset_done.html"),
         name ='password_reset_complete'),
]
