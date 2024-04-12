from django.shortcuts import render, HttpResponse
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
