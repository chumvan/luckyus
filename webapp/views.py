import json
from django.shortcuts import render
from .settings import BASE_DIR
# get the latest message from data/message.json


def get_latest_message() -> str:
    with open("data/message.json", "r") as f:
        messages = json.load(f)
    return messages[-1]["message"]


def message_view(request):
    message = get_latest_message()
    print(BASE_DIR)
    return render(request, "message.html", {"message": message})
