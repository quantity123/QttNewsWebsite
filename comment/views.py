from django.shortcuts import render, get_object_or_404
from article.models import Article
from .forms import CommentForm
from django.http import HttpResponse
from django.views.generic import RedirectView

class ArticleComment(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'article:articleDetail'
    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        if self.request.method == 'POST':
            commentForm = CommentForm(self.request.POST)
            if commentForm.is_valid():
                newComment = commentForm.save(commit=False)
                newComment.article = article
                newComment.user = self.request.user
                newComment.save()
                # self.url = article.get_absolute_url()
                return super(ArticleComment, self).get_redirect_url(*args, **kwargs)
            else:
                return HttpResponse('表单有错误。')
        else:
            return HttpResponse('评论只接收POST请求。')