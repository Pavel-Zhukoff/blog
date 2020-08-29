from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from blog.forms import ArticleForm
from blog.models import BlogModel, ArticleModel


@login_required(login_url=reverse_lazy('login'))
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('article-details', args=(ArticleModel.objects.latest('id').pk,)))
    else:
        form = ArticleForm()
        form.fields['blog'].queryset = BlogModel.objects.filter(user=request.user)

    data = {
        'title': 'Создание статьи',
        'form': form,
        'breadcrumbs': [
            {'url': reverse_lazy('article-new'), 'title': 'Создание статьи'},
        ]
    }
    return render(request,
                'views/blog/article_new.jhtml',
                data)


@login_required(login_url=reverse_lazy('login'))
def update_article(request, pk):
    article = ArticleModel.objects.get(pk=pk)
    if article.blog.user.id != request.user.id: return HttpResponseRedirect(reverse_lazy('home'))
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            updated_article = form.save(commit=False)
            updated_article.pk = article.pk
            updated_article.creation_date = article.creation_date
            updated_article.save()
            return HttpResponseRedirect(reverse_lazy('article-details', args=(article.pk,)))
    else:
        form = ArticleForm(instance=article)
        form.fields['blog'].queryset = BlogModel.objects.filter(user=request.user)
    data = {
        'title': 'Редактирование блога',
        'article': article,
        'form': form,
    }
    return render(request,
                  'views/blog/article_update.jhtml',
                  data)


def get_articles(request):
    data = {
        'title': 'Статьи',
        'articles': ArticleModel.objects.all().order_by('-creation_date'),
        'breadcrumbs': [
            {'url': reverse_lazy('article-list'), 'title': 'Статьи'}
        ]
    }

    return render(request,
                  'views/blog/article_list.jhtml',
                  data)


def get_article(request, pk):
    article = ArticleModel.objects.get(pk=pk)
    data = {
        'title': article.title,
        'article': article,
        'breadcrumbs': [
            {'url': reverse_lazy('blog-detail', args=(article.blog.id,)), 'title': article.blog.name},
            {'url': reverse_lazy('article-details', args=(article.pk,)), 'title': article.title},
        ]
    }
    return render(request,
                  'views/blog/article_details.jhtml',
                  data)
