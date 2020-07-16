from django.db import models

# DBからデータを取り出し、加工して、テンプレートに渡す

# Create your models here.
class Post(models.Model):
    # char型
    title = models.CharField(max_length=100)
    # 日付型
    published = models.DateTimeField()
    # 画像(引数で画像の格納先を指定)
    image = models.ImageField(upload_to='media/')
    #テキスト型
    body = models.TextField()

# 文字列をページに返す
    def __str__(self):
        return self.title
