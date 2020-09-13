from django import forms

from blog.blog import ArticleModel, TagModel, BlogModel


class ArticleForm(forms.ModelForm):

    title = forms.CharField(max_length=150,
                            label='Заголовок поста',
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-input',
                                }
                            )
                            )
    text = forms.CharField(max_length=500,
                           label='Текст поста',
                           required=True,
                           widget=forms.Textarea(
                               attrs={
                                   'class': 'form-input',
                               }
                           )
                           )
    blog = forms.ModelChoiceField(queryset=BlogModel.objects.all(),
                                    label='Блог',
                                    required=True,
                                    widget=forms.Select(
                                        attrs={
                                            'class': 'form-select',
                                        }
                                    )
                                    )
    tags = forms.ModelMultipleChoiceField(queryset=TagModel.objects.all(),
                                          label='Теги',
                                          required=True,
                                          widget=forms.SelectMultiple(
                                              attrs={
                                                  'class': 'form-select',
                                              }
                                          )
                                          )
    draft = forms.BooleanField(label='Черновик',
                               required=False,
                               widget=forms.CheckboxInput(
                                   attrs={
                                       'class': 'form-checkbox'
                                   }
                               )
                               )
    class Meta:
        model = ArticleModel
        fields = ['title', 'text', 'blog', 'tags', 'draft']
