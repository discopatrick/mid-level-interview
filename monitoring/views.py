from django.views.generic import ListView

from .models import Server


class ServerList(ListView):

    model = Server
