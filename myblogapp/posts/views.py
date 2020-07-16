from django.shortcuts import render
from django.http import HttpResponse
# postのクラス定義を読み込む
from .models import Post

# Create your views here.
def index(request):
    # return HttpResponse("Hello world")
    # -published = 公開日の降順にデータを呼ぶ
    posts = Post.objects.order_by('-published')
    # postsというデータにpostsという内容をもってtemplateエンジン(htmlファイルに引き渡す役割)に渡してあげる
    return render(request, 'posts/index.html', {'posts':posts})