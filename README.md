# README

## 方法


```sh

#アナコンダで環境作成(py36という名前で)
conda create -n py36

#環境を切り替える(py36に)
source activate py36

#py36環境にdjangoをインストール
conda install django

#conda環境の確認
conda info -e


```

## pythonについて

a/bの結果を整数で表示
a//b


文字連結
+

改行コード
print(d+"¥n"+e)
"¥n"

文字繰り返し
d*5
(dは文字)

文字の取り出し
d[7]
(dの8文字めを取り出す)

文字の取り出し
d[7:11]
(dの8-12文字めを取り出す)
(:はスライス。機械学習、webプログラミングによく使う)

文字数数える
len(d)

文字列型-> バイト型にする
    エンコード(符号化)
    >>> g.encode('utf-8')
    b'\xe3\x82\x86\xe3\x83\xbc\xe3\x81\xa7\xe3\x81\xbf\xe3\x83\xbc'
    >>> h = g.encode('utf-8')
    デコード(複合化)
    >>> h
    b'\xe3\x82\x86\xe3\x83\xbc\xe3\x81\xa7\xe3\x81\xbf\xe3\x83\xbc'
    >>> h.decode('utf-8')
    'ゆーでみー'


## django


$ pip install django==3.0.8

確認
import django
print(django.get_version())


アプリケーションの集まりがプロジェクト
各機能＝アプリケーション
アプリ(ユーザ管理、投稿管理、コメント管理、、、など)

```
#アプリ作成
$ django-admin startproject myblogapp
```

### ファイル説明
manage.py=djangoを操作するためのファイル

__init__.py

パイソンのプログラムだということを知らせる


urls.py
アプリケーションをどういうパターンのURLで呼ぶのか定義

wsgi.py
(web server gateway interface)
django内蔵サーバは遅い。
高速にうごくnginxなどと連携させる。
そのためのファイル。
その他のサーバと連携させるためのファイル。

### サーバ立ち上げ〜

```
python manage.py runserver
```

ブラウザにアクセス

データを移行する=migrate
```
python manage.py migrate
```

### アプリケーション作成

  python manage.py startapp posts
アプリの名前は複数形が良い

フォルダ説明

views.py
ページの整形

models.py
データベースとwebページを連携させる

#### アプリの存在をプロジェクトに知らせる
apps.pyの中に書いてある、
PostsConfigを呼び出せるようにする

setting.pyのなかのINSTALL_APPみたいなところに
    'posts.apps.PostsConfig',
を追加。
postsフォルダ、appsファイル、PostsConfigクラスを呼び出し

path(ulrパターン,ビュー関数)

#### ルーティング

プロジェクトのルーティング(urls.py)
myblogapps.ulrs
↓
アプリ内のルーティング(urls.py)
posts.urls
↓
viewsファイルの中のindex関数
views.index

(アプリの中のurls.pyファイルは自分で作る。)

※import
他のファイルを使うときはinclude記載する

#### templateファイルを使ってみる

views.pyにtemplatesフォルダの中のファイルを指定して、呼び出す


#### modelsを使ってみる

models内にクラスを作成<br>
↓<br>
コンソールから、makemigrationsでDBのテーブル作成ファイルを作成<br>
↓<br>
コンソールから、migrateでDBのテーブル作成<br>


データベース内のデータをあたかも一つの変数のように使用することができる

modelsの中のクラス＝データと命令(更新、削除など？)をセットで扱う変数のテンプレート

object=クラスから生成された各データ

書き方例：
```py
    # char型
    title = models.CharField(max_length=100)
    # 日付型
    published = models.DateTimeField()
    # 画像(引数で画像の格納先を指定)
    image = models.ImageField(upload_to='media/')
    #テキスト型
    body = models.TextField()

```


```sh
# 新しく定義ファイルがあった場合、それをDBに投入するためのファイルを自動生成する。
python manage.py makemigrations
```
自動生成されたファイルは、migrationの中に格納されている。

```sh
# 自動生成されたファイルを実行して、テーブルを作成
python manage.py migrate
```


#### sqlite

sqliteコマンド
```sh
#DBに接続
sqlite3 db.sqlite3
#SQL文

#table表示
.table

#select
select * from posts_post ;

#終了
.exit

```

#### admin

公開するならadmin以外の名前をつける！（セキュリティてきに）
adminじゃないのをつけた
```
 python manage.py createsuperuser

```

adminサイトから投稿できるようにする
postsフォルダのadmin.pyを編集

#### templateエンジン

djangoに内蔵されているtemplate Engineには2種類ある
- django
- Jinja 2
    template ->  template = 寺 -> 神社　らしい笑

DBから取り出した値を変数としてtemplate Engineに渡すと、
htmlファイルに渡してくれる。
静的なページ(画像など)だけでなく、動的なページを実現することもできる。

テンプレートエンジンの記法：
curly bracketカーリーブラケット＝　{% %} 


```html
<!-- postsの全てのデータを取り出す。 -->
<!-- タイトルを表示する。 -->
        {% for post in posts.all %}

            {{post.title}}

        {% endfor %}
```

#### staticなデータ
staticの設定はちょっとややこしい。。。


staticなデータとは＝映像、画像　など

今回は画像

htmlではimgタグで指定

呼び出すURL設定　＋　フォルダ指定
が必要

BASE_DIRはsetting.pyで設定されている、osにpythonのプロジェクトがどこにあるか知らせているディレクトリ

今回'pics'というURLを動的なURLとして仮想的に作成している！

アプリ以外のファイルで、
- settingの変更 (MEDIA_ROOTとMEDIA_URLの設定)
- urlの変更(static)

が必要！！


#### 投稿の詳細ページに遷移できるようにする

投稿一覧
投稿詳細

投稿タイトルをクリックして、投稿詳細に遷移する機能を実装


URLは　　http://127.0.0.1:8000/posts/{posts.id}
のようにすることを考える



get_object_or_404

をインポートするのは便利そう！！
オブジェクトがなければ404を返すという機能が実装できる

    post = Post.objects.get(pk=post_id)

↓

