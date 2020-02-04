import datetime
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from article.models import Article, Category
from django.urls import reverse

class ArticleModeTests(TestCase):
    def test_was_createdTime_recently_with_future_article(self):
        author = User(username='user1', password='test_password1')
        author.save()
        future_article = Article(author=author, title='test1', body='test1', createdTime=timezone.now()+datetime.timedelta(days=30))
        self.assertIs(future_article.was_createdTime_recently(), False)
    def test_was_createdTime_recently_with_seconds_before_article(self):
        author = User(username='user2', password='test_password2')
        author.save()
        seconds_before_article = Article(author=author, title='test2', body='test2', createdTime=timezone.now()-datetime.timedelta(seconds=45))
        self.assertIs(seconds_before_article.was_createdTime_recently(), True)

class ArticleViewTests(TestCase):
    def test_increase_viewCount(self):
        author = User(username='user3', password='test_password3')
        author.save()
        category = Category(name='分类3')
        category.save()
        article = Article(title='test3', body='test3', author=author, category=category)
        article.save()
        self.assertIs(article.viewCount, 0) # 判断初始化浏览量是否是0
        url = reverse('article:articleDetailView', args=(article.id,))
        self.client.get(url)  # 浏览一次这个新闻
        viewCountArticle = Article.objects.get(id=article.id)
        self.assertIs(viewCountArticle.viewCount, 1)  # 判断浏览量是否是1