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

    return render(request,
                'views/blog/article_new.jhtml',
                {'form': form})