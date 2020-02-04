from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Category(models.Model):
    name = models.CharField('分类名称', max_length=100)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['pk']
    def __str__(self):      # 当html模板用{{ 分类实例对象 }}取值时候调用__str__函数返回值
        return self.name

class Tag(models.Model):
    name = models.CharField('标签名称', max_length=100)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['pk']
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    category = models.ForeignKey(Category, verbose_name='分类', related_name='article', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    viewCount = models.PositiveIntegerField(default=0, editable=False)
    commentCount = models.PositiveIntegerField(default=0, editable=False)
    iconograph = models.ImageField(upload_to='articleIconograph/', blank=True)
    topRecommend = models.BooleanField(verbose_name='推荐', default=False)
    createdTime = models.DateTimeField('创建时间', default=timezone.now)
    modifiedTime = models.DateTimeField('修改时间', auto_now=True)  # auto_now 每次数据更新时自动写入当前时间
    author = models.ForeignKey(User, verbose_name='作者', related_name='article', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-createdTime']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article:articleDetail', args=(self.id,))
    def increase_viewCount(self):
        self.viewCount += 1
        self.save(update_fields=['viewCount'])
    def save(self, *args, **kwargs):
        article = super(Article, self).save(*args, **kwargs)
        if self.iconograph and not kwargs.get('update_fields'):
            image = Image.open(self.iconograph)
            x, y = image.size
            newX = 820
            newY = 400
            resizedImage = image.resize((newX, newY), Image.ANTIALIAS)
            resizedImage.save(self.iconograph.path)
        return article
    def was_createdTime_recently(self):
        diff = timezone.now() - self.createdTime
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            return True
        else:
            return False