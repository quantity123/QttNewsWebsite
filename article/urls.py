from django.urls import path
from .views import ArticleDetail, Home, About, CategoryArticleList, TagArticleList, SearchArticleList

app_name = 'article'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('searcharticlelist/', SearchArticleList.as_view(), name='searchArticleList'),
    path('categoryarticlelist/<int:pk>', CategoryArticleList.as_view(), name='categoryArticleList'),
    path('tagarticlelist/<int:pk>', TagArticleList.as_view(), name='tagArticleList'),
    path('articledetail/<int:pk>/', ArticleDetail.as_view(), name='articleDetail'),     # pk主键用在django类视图
    path('about/', About.as_view(), name='about'),
]