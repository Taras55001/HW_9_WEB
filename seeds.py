import json

from connect import session_hw
from models import Autor, Post, Tag

autors_json = "./autors.json"
post_json = "./quotes.json"


def list_data(file_name):
    with open(file_name, "r", encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def create_autor(data):
    autor = Autor(**{k: v for k, v in data.items()})
    autor.save()
    return autor


def crate_post(data):
    text = data.get("quote")
    tags_list = []
    for tag in data.get("tags"):
        tags_list.append(Tag(name=tag))
    autor = Autor.objects(fullname=data.get("author")).first()
    post = Post(quote=text,tags=tags_list, author=autor)
    post.save()


if __name__ == '__main__':
    session_hw
    # autors = list_data(autors_json)
    # for autor in autors:
    #     create_autor(autor)
    posts = list_data(post_json)
    for post in posts:
        crate_post(post)