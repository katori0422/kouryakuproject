from django.db import models
from django.conf import settings

class KouryakuPost(models.Model):
    '''モデルクラス adminで投稿
    '''
    #　カテゴリに設定する項目を入れ子のタプルとして定義
    #　タプルの第1要素はモデルが使用する値
    #　第2要素は管理サイトの選択メニューに表示する文字列
    CATEGORY = (('character', 'キャラクターのこと'),
                ('enemy', '敵のこと'),
                ('item', 'アイテムのこと'))
    
    #タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル', #フィールドのタイトル
        max_length=400 #最大文字数は200
    )
#　本文用のフィールド
    content = models.TextField(
    verbose_name='本文' #　フィールドのタイトル
    )
#　投稿日時のフィールド
    posted_at = models.DateTimeField(
    verbose_name='投稿日時', #　フィールドのタイトル
    auto_now_add=True #　日時を自動追加
    )
#　カテゴリのフィールド
    category = models.CharField(
    verbose_name='カテゴリ',
    max_length=50,
    choices=CATEGORY
    # catagoryフィールドにはCATEGORYの要素のみを登録
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='投稿者'
    )

    def __str__(self):
        '''Django管理サイトでデータを表示する際に識別名として
            投稿日時のタイトル(titleフィールドの値)を表示するために必要
        
        Returns(str):投稿日時のタイトル
        '''
        return self.title
    
'''掲示板での投稿'''


class Post(models.Model):
    # カテゴリの選択肢を定義
    CATEGORY_CHOICES = [
        ('character', 'キャラクター'),
        ('enemy', '敵'),
        ('item', 'アイテム'),
    ]

    title = models.CharField(max_length=100)  # 投稿のタイトル
    content = models.TextField()             # 投稿の本文
    category = models.CharField(
        max_length=10,  # 最大文字数
        choices=CATEGORY_CHOICES,  # 選択肢
    )
    created_at = models.DateTimeField(auto_now_add=True)  # 投稿日時

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"