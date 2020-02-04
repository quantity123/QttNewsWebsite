from .models import Article, Category, Tag
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from comment.models import Comment
from django.shortcuts import render, get_object_or_404

class CommonList(ListView):
    model = Article
    context_object_name = 'articleList'
    template_name = 'article/articleList.html'
    paginate_by = 10  # 一页显示10个记录
    def get_queryset(self):
        self.order = self.request.GET.get('order')   # ?后面根据键获取值
        if self.order == 'hot_order':
            return super(CommonList, self).get_queryset().order_by('-viewCount')
        else:
            return super(CommonList, self).get_queryset()
    def get_context_data(self, **kwargs):
        context = super(CommonList, self).get_context_data(**kwargs)
        context['categoryList'] = Category.objects.all()
        context['tagList'] = Tag.objects.all()
        context['order'] = self.order
        return context

class Home(CommonList):
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['topRecommendArticleList'] = super(Home, self).get_queryset().filter(topRecommend=True)
        context['filterType'] = 0
        return context

class SearchArticleList(CommonList):
    def get_queryset(self):
        self.searchText = self.request.GET.get('searchText')
        return super(SearchArticleList, self).get_queryset().filter(Q(title__icontains=self.searchText)|Q(body__icontains=self.searchText))
    def get_context_data(self, **kwargs):
        context = super(SearchArticleList, self).get_context_data(**kwargs)
        context['filterType'] = 1
        context['searchText'] = self.searchText
        return context

class CategoryArticleList(CommonList):
    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs.get('pk'))   # url 内部获取参数值
        return super(CategoryArticleList, self).get_queryset().filter(category=self.category)
    def get_context_data(self, **kwargs):
        context = super(CategoryArticleList, self).get_context_data(**kwargs)
        context['filterType'] = 2
        context['category'] = self.category
        return context

class TagArticleList(CommonList):
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagArticleList, self).get_queryset().filter(tag=self.tag)
    def get_context_data(self, **kwargs):
        context = super(TagArticleList, self).get_context_data(**kwargs)
        context['filterType'] = 3
        context['tag'] = self.tag
        return context

class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'articleDetail'
    template_name = 'article/articleDetail.html'
    def get_object(self, queryset=None):
        articleDetail = super(ArticleDetail, self).get_object(queryset=None)
        articleDetail.increase_viewCount()
        return articleDetail
    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['categoryList'] = Category.objects.all()
        context['tagList'] = Tag.objects.all()
        context['commentList'] = Comment.objects.filter(article=self.object.id)
        return context

class About(TemplateView):
    template_name = 'article/about.html'