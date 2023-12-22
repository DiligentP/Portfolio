from django.shortcuts import *
from .utils import *


def index(request):
    return redirect('about/')


def about(request):
    # makrdown 파일을 HTML로 변환합니다.
    html = mark('About.md')

    return render(request, "content.html", {'mark': html})


def portfolio(request):
    # makrdown 파일을 HTML로 변환합니다.
    html = mark('Portfolio.md')

    return render(request, "content.html", {'mark': html})


def activity(request):
    # makrdown 파일을 HTML로 변환합니다.
    html = mark('Activity.md')

    return render(request, "content.html", {'mark': html})


def skill(request):
    # makrdown 파일을 HTML로 변환합니다.
    html = mark('Skill.md')

    return render(request, "content.html", {'mark': html})
