from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.forms import ArticleCreationForm
from blog.models import BlogModel, ArticleModel


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/{}'.format(ArticleModel.objects.latest('id').pk))
    else:
        form = ArticleCreationForm()
        form.fields['blog'].queryset = BlogModel.objects.filter(user=request.user)

    data = {
        'form': form,
        'breadcrumbs': [
            {'url': '/article/new', 'title': 'Создание статьи'},
        ]
    }
    return render(request,
                'views/blog/article_new.jhtml',
                data)

def get_article(request, pk):
    article = ArticleModel.objects.get(pk=pk)
    data = {
        'article': article,
        'breadcrumbs': [
            {'url': '/blog/{}'.format(article.blog_id), 'title': article.blog.name},
            {'url': '/article/{}'.format(article.pk), 'title': article.title},
        ]
    }
    return render(request,
                  'views/blog/article_details.jhtml',
                  data)