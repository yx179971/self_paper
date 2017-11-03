from django.shortcuts import render
from django.forms import ModelForm
from . import models


def user_add_paper(request):
    return render(request, 'user_add_paper.html', )
