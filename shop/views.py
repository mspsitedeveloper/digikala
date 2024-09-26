from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import DetailView , CreateView ,View , FormView , ListView
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse_lazy , reverse
from .models import Product, Category , Commentshop
from .forms import ProductForm ,Comment_Form
from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin
from django.core.paginator import Paginator

class Home(View):
    model = Product
    template_name = 'shop.html'
    paginate_by = 3

    def get(self, request):
        posts = Product.objects.all()
        paginator = Paginator(posts, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context ={
            'product_list' : page_obj
        }
        return render(request , self.template_name , context)
    
class commentget(DetailView):
    model = Product
    template_name = 'single-shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Comment_Form
        return context

class commentpost(SingleObjectMixin, FormView):
    model = Product
    form_class = Comment_Form
    template_name = 'single-shop.html'
    def post(self , request, *args , **kwargs):
        self.object = self.get_object()
        return super().post(request , *args , **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit = False)
        comment.author = self.request.user
        comment.product = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        post = self.get_object()
        return reverse("single", kwargs= {"slug" : post.slug })

class Single(View):
    def get(self , request , *args , **kwargs):
        view = commentget.as_view()
        return view(request,*args , **kwargs)
    
    def post(self , request , *args , **kwargs):
        view = commentpost.as_view()
        return view(request, *args , **kwargs)

class NewProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'new_product.html'    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.extract = post.body[:100]
        post.save()
        return super().form_valid(form)
class UpdatePost(UpdateView):
    model = Product
    template_name = 'update_product.html'
    fields = ['name', 'desc', 'photo' , 'Price' , 'category']
    def form_valid(self, form):
        post = form.save(commit=False)
        post.extrtact = post.desc[:100]
        post.save()
        return super().form_valid(form)
    def get_success_url(self):
        post = self.get_object()
        return reverse("single", kwargs= {"slug" : post.slug })

class DeletePost(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('success')