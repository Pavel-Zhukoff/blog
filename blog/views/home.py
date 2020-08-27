
from django.views import View
from django.shortcuts import render

from blog.models import ArticleModel, BlogModel


class HomeView(View):

    def get(self, request):
        last_articles = ArticleModel.objects.filter(draft=False)[:5]
        if self.request.user.is_authenticated:
            user_blogs = BlogModel.objects.filter(user=self.request.user)
        else:
            user_blogs = []
        return render(
            request,
            'views/blog/home.jhtml',
            {'title': 'Главная', 'last_articles': last_articles, 'user_blogs': user_blogs}
        )