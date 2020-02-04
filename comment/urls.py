from django.urls import path
from .views import ArticleComment

app_name = 'comment'

urlpatterns = [
    path('articlecomment/<int:pk>', ArticleComment.as_view(), name='articleComment'),
]