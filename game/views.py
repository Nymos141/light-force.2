from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from game.models import Product, Feedback
from django.shortcuts import render, redirect
from django.db import models
from django.db.models import Q
from game.forms import FeedbackForm, ProductForm
from django.urls import reverse
import random
import datetime


def hello_views(request):
    if request.method == "GET":
        return HttpResponse("hello")

class Hello(View):
    def get(self, request):
        return HttpResponse("Hello Everybody")

def jokes_views(request):
    if request.method == "GET":
        jokes = [
            "My love is like communism; everyone gets a share, and it's only good in theory.",
            "Money talks… but all mine ever says is good-bye.",
            "Student: Brains like Bermuda triangle – when information goes in it is never found again.",
            "Hardwork never killed anybody, but why take a chance?",
            "I always learn from the others’ mistakes.",
            "Goblin is a proud bird, until you kick it it will not fly."
        ]
        joke = random.choice(jokes)
        return HttpResponse(joke)

class JokesView(View):
    def get(self, request):
        jokes = [
            "My love is like communism; everyone gets a share, and it's only good in theory.",
            "Money talks… but all mine ever says is good-bye.",
            "Student: Brains like Bermuda triangle – when information goes in it is never found again.",
            "Hardwork never killed anybody, but why take a chance?",
            "I always learn from the others’ mistakes.",
            "Goblin is a proud bird, until you kick it it will not fly."
        ]
        joke = random.choice(jokes)
        return HttpResponse(joke)

def main_views(request):
    now = datetime.datetime.now()
    jokes = [
        "My love is like communism; everyone gets a share, and it's only good in theory.",
        "Money talks… but all mine ever says is good-bye.",
        "Student: Brains like Bermuda triangle – when information goes in it is never found again.",
        "Hardwork never killed anybody, but why take a chance?",
        "I always learn from the others’ mistakes.",
        "Goblin is a proud bird, until you kick it it will not fly."
    ]
    random_joke = random.choice(jokes)

    context = {
        "current_date": now.date(),
        "current_time": now.time(),
        "greetings": "Elune-adore",
        "random_joke": random_joke
    }
    if request.method == 'GET':
        return render(request, "homepage.html", context)

class MainView(View):
    def get(self, request):
        now = datetime.datetime.now()
        jokes = [
            "My love is like communism; everyone gets a share, and it's only good in theory.",
            "Money talks… but all mine ever says is good-bye.",
            "Student: Brains like Bermuda triangle – when information goes in it is never found again.",
            "Hardwork never killed anybody, but why take a chance?",
            "I always learn from the others’ mistakes.",
            "Goblin is a proud bird, until you kick it it will not fly."
        ]
        random_joke = random.choice(jokes)

        context = {
            "current_date": now.date(),
            "current_time": now.time(),
            "greetings": "Elune-adore",
            "random_joke": random_joke
        }
        return render(request, "homepage.html", context)

class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"


def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        print(products)
        return render(request, "products/product_list.html",
                      {"products": products})

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
    context_object_name = "detail"

    def post(self, request, *args, **kwargs):
        product_id = kwargs['pk']
        product = get_object_or_404(Product, pk=product_id)
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.instance.product = product
            form.save()
            return redirect('detail_product', product_id=product_id)
        return self.render_to_response(self.get_context_data(form=form))


def detail_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    feedbacks = Feedback.objects.filter(product_id=product_id)

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.instance.product = product
            form.save()
            return redirect('detail_product', product_id=product_id)
    else:
        form = FeedbackForm()

    context = {'detail': product, 'feedbacks': feedbacks, 'form': form}
    return render(request, "products/detail.html", context)

class AddFeedbackView(View):
    def post(self, request, product_id):
        if request.method == 'POST':
            text = request.POST.get('text')
            return redirect('detail_product', product_id=product_id)
        else:
            return HttpResponse("error")

def add_feedback(request, product_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        return redirect('detail_product', product_id=product_id)
    else:
        return HttpResponse("erorr")

class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/create_product.html"
    success_url = "/product_list"

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "products/create_product.html", {"form": form})

class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/edit.html"

    def form_valid(self, form):
        product_id = self.kwargs['pk']
        product = Product.objects.get(id=product_id)
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_product', kwargs={'product_id': self.kwargs['pk']})

def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Нет продукта с таким названием ', status=404)

    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(request, "products/edit.html", {"form": form})

    elif request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('detail_product', kwargs={'product_id': product_id}))

        return render(request, "products/edit.html", {"form": form})

