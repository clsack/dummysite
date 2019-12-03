# Standard library imports
import logging

# Related third party imports


# Local application/library specific imports
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
logger = logging.getLogger(__name__)


@login_required
def error_404_view(request, exception):
    return render(request, '404.html', status=404)


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def logout_view(request):
    logout(request)
