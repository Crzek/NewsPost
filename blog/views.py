# global var
from dotenv import load_dotenv

from .models import Post
from .forms import AddPostForm

from django.shortcuts import render

from requests.exceptions import HTTPError

import datetime
import requests
import os
import datetime


load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
print("apikey ***", API_KEY)

POST = []


def index(request):
    # Your code here
    today = datetime.date.today()

    url = (
        'https://newsapi.org/v2/top-headlines?'
        'country=us&'
        f'from={today}&'  # YYYY-MM-DD
        #    'sortBy=popularity&'
        f'apiKey={API_KEY}')

    print("*******", url)
    print(today)
    articles = []

    try:
        response = requests.get(url)
        if response.status_code == 200:
            r_json: dict = response.json()
            if r_json["totalResults"] != 0:
                # articles = r_json["articles"][:20]
                for index, article in enumerate(r_json["articles"], 1):
                    if article["title"] and article["content"]:
                        article["id"] = index
                        articles.append(article)

                        new_post = Post(
                            title=article["title"],
                            body=article["content"],
                            description=article["description"],
                            date=today
                        )
                        new_post.save()

                    if len(articles) == 20:
                        POST = articles
                        break

        else:
            raise HTTPError(response.status_code)

    except requests.exceptions.RequestException as e:
        # Maneja errores de solicitud y problemas de red aquí
        print(f"Error en la solicitud HTTP: {e}")

    context = {
        "articles": articles,
        "date": today,
    }

    return render(request, "blog.html", context=context)


def add_post(request):
    # Your code here
    context = {}
    return render(request, "add_post.html", context)


def post(request, article_id):
    if POST:
        article = POST[article_id]

    else:
        article = Post.objects.get(id=article_id)

    return render(
        request,
        "post.html",
        context={
            "article": article,
            "date": datetime.date.today()
        })
