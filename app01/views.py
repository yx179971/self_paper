from django.shortcuts import render


def preview(request):
    print(request.GET)
    return render(request, 'preview.html')


def detail(request):
    return render(request, 'arya/detail.html')
