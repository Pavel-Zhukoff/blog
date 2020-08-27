from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from blog.models import BlogModel, ArticleModel


class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = 'views/blog/blog_new.jhtml'
    fields = ['name']
    model = BlogModel

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(BlogCreateView, self).form_valid(form)

class BlogIdDetailView(DetailView):
    template_name = 'views/blog/blog_details.jhtml'
    model = BlogModel

    def get_context_data(self, **kwargs):
        context = super(BlogIdDetailView, self).get_context_data(**kwargs)
        context['articles'] = ArticleModel.objects.filter(blog=self.object)
        return context

class BlogAuthorListView(ListView):
    template_name = 'views/blog/blog_list.jhtml'
    model = BlogModel
    context_object_name = 'blog_list'

    def get_queryset(self):
        return BlogModel.objects.filter(user__username=self.kwargs['username'])

class BlogListView(ListView):
    template_name = 'views/blog/blog_list.jhtml'
    model = BlogModel
    context_object_name = 'blog_list'
