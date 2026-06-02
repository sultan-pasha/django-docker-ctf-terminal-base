from django.urls import re_path
from terminal.consumer import TerminalConsumer  # Explicit absolute path import


websocket_urlpatterns = [
    re_path(r"ws/terminal/$", TerminalConsumer.as_asgi()),
]