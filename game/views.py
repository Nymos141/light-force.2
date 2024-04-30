from django.shortcuts import render, HttpResponse, get_object_or_404
from game.models import Product, MyModelManager, Feedback
from django.shortcuts import render, redirect
from django.db import models
from game.forms import FeedbackForm
import random
import datetime


def hello_views(request):
    if request.method == "GET":
        return HttpResponse("hello")

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

def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        print(products)
        return render(request, "products/products_list.html",
                      {"products": products})


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

def add_feedback(request, product_id):
    if request.method == "POST":
        text = request.POST.get('text')
        product = get_object_or_404(Product, pk=product_id)
        feedback = Feedback.objects.create(product=product, text=text)
        return redirect('detail_product', product_id=product_id)
    else:
        return redirect('detail_product', product_id=product_id)
def create_product(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        product = Product.objects.create(title=title, text=text, image=image, price=price)
        return HttpResponse("Продукт успешно создан")
    else:
        return render(request, "products/create_product.html")