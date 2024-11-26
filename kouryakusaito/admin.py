from django.contrib import admin
from .models import KouryakuPost

# Django管理サイトにKoouryakuPostを登録する
class KouryakuPostAdmin(admin.ModelAdmin):
    # 投稿者をリストに追加
    list_display = ('title', 'author', 'posted_at', 'category')
    # フィルタリングを有効にする（投稿者でフィルタリングできるように）
    list_filter = ('author', 'category')
    # 検索を有効にする（投稿者の名前でも検索できるように）
    search_fields = ('title', 'content', 'author__username')

# モデルの管理画面をカスタマイズ
admin.site.register(KouryakuPost, KouryakuPostAdmin)