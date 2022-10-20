from django.shortcuts import render, HttpResponse

# Create your views here.
# FBV模式
# def book(request):
#     if request.method == 'GET':
#         return HttpResponse('get....')
#     else:
#         return HttpResponse('post....')


# CBV模式

# from django.views import View
#
# class BookView(View):
#     def get(self, request):
#         return HttpResponse('views get....')
#     def post(self, request):
#         return HttpResponse('views post...')


# APIview模式

from rest_framework.views import APIView


class BookView(APIView):
    def get(self, request):
        return HttpResponse('APIviews get....')

    def post(self, request):
        return HttpResponse('APIviews post...')
