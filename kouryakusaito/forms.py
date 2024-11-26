#
from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import Post
from .models import KouryakuPost

class ContactForm(forms.Form):
    #
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        #
        super().__init__(*args, **kwargs)
        #
        self.fields['name'].widget.attrs['placeholder'] = \
            'お名前を入力してください'
        #
        self.fields['name'].widget.attrs['class'] = 'form-control'

        #
        self.fields['email'].widget.attrs['placeholder'] = \
            'メールアドレスを入力してください'
        #
        self.fields['email'].widget.attrs['class'] = 'form-control'

        #
        self.fields['title'].widget.attrs['placeholder'] = \
            'タイトルを入力してください'
        #
        self.fields['title'].widget.attrs['class'] = 'form-control'

        #
        self.fields['message'].widget.attrs['placeholder'] = \
            'メッセージを入力してください'
        #
        self.fields['message'].widget.attrs['class'] = 'form-control'

'''掲示板の投稿'''

'''
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']  # 必要なフィールドを定義
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'タイトルを入力'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '本文を入力'}),
            'category': forms.Select(attrs={'class': 'form-control'}),  # カテゴリ用の選択フォーム
        }
'''
class PostForm(forms.ModelForm):
    class Meta:
        model = KouryakuPost
        fields = ['title', 'content', 'category']