
from django.views import View
from django.shortcuts import render

from blog.models import ArticleModel

class HomeView(View):

    def get(self, request):
        last_articles = ArticleModel.objects.filter(draft=False)[:5]
        return render(
            request,
            'views/blog/home.jhtml',
            {'title': 'Главная', 'last_articles': last_articles}
        )