from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import DetailView , CreateView ,View , FormView , ListView
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse_lazy , reverse
from .models import Post , comment
from .forms import PostForm ,commentForm , SearchForm
from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin
from django.core.paginator import Paginator

class Home(View):
    model = Post
    template_name = 'blog.html'
    paginate_by = 3

    def get(self, request):
        posts = Post.objects.all()
        paginator = Paginator(posts, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context ={
            'post_list' : page_obj
        }
        return render(request , self.template_name , context)

class Search(ListView):
    template_name = 'search.html'
    model = Post
    form_class = SearchForm

    def get(self , request):
        posts = Post.objects.all()
        if 'search' in request.GET :
            form_class = SearchForm(request.GET)
            if form_class.is_valid():
                cd = form_class.cleaned_data['search']
                posts = posts.filter(title=cd)
        context = {
            'post_list' : posts
        }
        return render(request , self.template_name , context)

class commentget(DetailView):
    model = Post
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = commentForm
        return context

class commentpost(SingleObjectMixin, FormView):
    model = Post
    form_class = commentForm
    template_name = 'single.html'
    def post(self , request, *args , **kwargs):
        self.object = self.get_object()
        return super().post(request , *args , **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit = False)
        comment.author = self.request.user
        comment.post = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        post = self.get_object()
        return reverse("single", kwargs= {"pk" : post.pk })

class Single(View):
    def get(self , request , *args , **kwargs):
        view = commentget.as_view()
        return view(request,*args , **kwargs)
    
    def post(self , request , *args , **kwargs):
        view = commentpost.as_view()
        return view(request, *args , **kwargs)

class NewPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.abstract = post.body[:100]
        post.save()
        return super().form_valid(form)
class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'abstract', 'body', 'photo']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')