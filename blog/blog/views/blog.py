from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from blog.blog import BlogModel, ArticleModel


class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = 'views/blog/blog_new.jhtml'
    fields = ['name']
    model = BlogModel

    login_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(BlogCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BlogCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание блога'
        context['breadcrumbs'] = [
            {'url': reverse_lazy('blog-new'), 'title': 'Создание блога'},
        ]
        return context


class BlogIdDetailView(DetailView):
    template_name = 'views/blog/blog_details.jhtml'
    model = BlogModel

    def get_context_data(self, **kwargs):
        context = super(BlogIdDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Блог: {}'.format(self.object.name)
        context['articles'] = ArticleModel.objects.filter(blog=self.object)
        context['breadcrumbs'] = [
            {'url': reverse_lazy('blog-detail', args=(self.object.id,)), 'title': self.object.name},
        ]
        return context

class BlogAuthorListView(ListView):
    template_name = 'views/blog/blog_list.jhtml'
    model = BlogModel
    context_object_name = 'blog_list'

    def get_queryset(self):
        return BlogModel.objects.filter(user__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super(BlogAuthorListView, self).get_context_data(**kwargs)
        context['title'] = 'Блоги автора {}'.format(self.kwargs['username'])
        context['breadcrumbs'] = [
            {
                'url': reverse_lazy('blog-list-author', args=(self.kwargs['username'],)),
                'title': ' Блоги автора {}'.format(self.kwargs['username'])
            },
        ]
        return context

class BlogListView(ListView):
    template_name = 'views/blog/blog_list.jhtml'
    model = BlogModel
    context_object_name = 'blog_list'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['title'] = 'Список блогов'
        context['breadcrumbs'] = [
            {'url': reverse_lazy('blog-list'), 'title': ' Блоги'},
        ]
        return context
