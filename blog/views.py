from django.shortcuts import render
from django.http import HttpResponse

def portao(request):
    return HttpResponse('Você chegou ao portão da casa !')

def sala(request):
    return HttpResponse('Você chegou à sala da casa. Senta ai no sofá!')

def quarto(request):
    return HttpResponse('Você chegou ao quarto da casa. Vai dormir?')

def post_list(request):
    return render(request, 'blog/post_list.html', {}) 