from django.db import models
from article.models import Article
from django.contrib.auth.models import User

class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name='新闻文章', on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=models.CASCADE, related_name='comment')
    text = models.TextField('评论内容')
    createdTime = models.DateTimeField('创建时间', auto_now_add=True)
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ('createdTime',)
    def __str__(self):
        return '{}: {}'.format(self.user, self.text[:20])