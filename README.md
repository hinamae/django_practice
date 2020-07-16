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

