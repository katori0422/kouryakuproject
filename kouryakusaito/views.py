from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import KouryakuPost
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .forms import PostForm
from django.http import HttpResponseForbidden
from .models import Post

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'orderby_records'
    queryset = KouryakuPost.objects.order_by('-posted_at')
    paginate_by = 4

class KouryakuDetail(DetailView):
    template_name = 'post.html'
    model = KouryakuPost


class CharacterView(ListView):
    template_name = 'character.html'
    context_object_name = 'character_records'
    queryset = KouryakuPost.objects.filter(
        category='character').order_by('-posted_at')
    paginate_by = 3

class EnemyView(ListView):
    template_name = 'enemy.html'
    context_object_name = 'enemy_records'
    queryset = KouryakuPost.objects.filter(
        category='enemy').order_by('-posted_at')
    paginate_by = 3

class ItemView(ListView):
    template_name = 'item.html'
    context_object_name = 'item_records'
    queryset = KouryakuPost.objects.filter(
        category='item').order_by('-posted_at')
    paginate_by = 2
'''
class KeijibanView(ListView):
    template_name = 'keijiban.html'
    context_object_name = 'orderby_records'
    queryset = KouryakuPost.objects.order_by('-posted_at')
    paginate_by = 4
'''
class KeijibanView(ListView):
    template_name = 'keijiban.html'
    context_object_name = 'orderby_records'
    queryset = KouryakuPost.objects.order_by('-posted_at')
    paginate_by = 5

class GamesystemView(ListView):
    template_name = 'gamesystem.html'
    context_object_name = 'gamesystem_records'
    queryset = KouryakuPost.objects.filter(
        category='item').order_by('-posted_at')
    paginate_by = 2

#P291
class ContactView(FormView):
    template_name ='contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('kouryakusaito:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message= form.cleaned_data['message']

        subject = 'お問い合わせ: {}'.format(title)
        
        message = \
        '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:\n{3}'\
        .format(name, email, title, message)
        from_email = 'tdn2430108@stu.o-hara.ac.jp'
        to_list = ['tdn2430108@stu.o-hara.ac.jp']
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                              )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
    
def keijiban_view(request):
    records = KouryakuPost.objects.order_by('-posted_at')
    return render(
        request, 'keijiban.html', {'orderby_records': records})

def kouryaku_detail(request, pk):
    record = KouryakuPost.objects.get(id=pk)
    return render(
        request, 'post.html', {'object': record})

'''
def user_posts(request, user_id):
    # ユーザーを取得（404エラーを防ぐためにget_object_or_404を使用）
    user = get_object_or_404(User, id=user_id)
    
    # そのユーザーが投稿した投稿のみを取得
    posts = KouryakuPost.objects.filter(author=user)

    # テンプレートにデータを渡す
    return render(request, 'user_posts.html', {'posts': posts, 'user': user})
'''

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user  # ログインユーザーを投稿者として設定
            form.save()
            return redirect('kouryakusaito:keijiban')  # 一覧ページなど適切なURLへリダイレクト
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

class PostListView(ListView):
    model = KouryakuPost
    template_name = 'kouryakusaito/keijiban.html'  # 一覧ページに使用するテンプレート
    context_object_name = 'orderby_records'  # テンプレート内で使う変数名
    paginate_by = 10  # 1ページに表示する投稿数


def delete_post(request, pk):
    post = get_object_or_404(KouryakuPost, pk=pk)

    # 投稿者が現在ログインしているユーザーであるか確認
    if post.author != request.user:
        return HttpResponseForbidden("あなたはこの投稿を削除する権限がありません。")

    if request.method == 'POST':
        post.delete()  # 投稿を削除
        return redirect('kouryakusaito:keijiban')  # 削除後、掲示板一覧にリダイレクト
    
    return render(request, 'delete_post.html', {'post': post})  # 確認用テンプレートを表示
'''
def keijiban(request):
    category = request.GET.get('category')  # URLからカテゴリを取得
    if category:
        posts = Post.objects.filter(category=category)
    else:
        posts = Post.objects.all()
    return render(request, 'keijiban.html', {'posts': posts, 'selected_category': category})
'''
def keijiban_by_category(request, category):
    posts = Post.objects.filter(category=category)  # 指定カテゴリの投稿を取得
    return render(request, 'keijiban.html', {'posts': posts, 'selected_category': category})

