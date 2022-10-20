from django.shortcuts import render, HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView
from .models import BookView
from rest_framework.response import Response


# Create your views here.
# 针对模型设计序列化器
# 继承serializers.Serializer
# class BooksSerilizers(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#     author = serializers.CharField(max_length=32)
#     pub_date = serializers.DateField()
#
#     def create(self, validated_data):
#         # 添加数据逻辑
#         new_book = BookView.objects.create(**validated_data)
#         return new_book
#
#     def update(self, instance, validated_data):
#         # 更新数据逻辑
#         BookView.objects.filter(id=instance.pk).update(**validated_data)
#         updated_book = BookView.objects.filter(id=instance.pk).first()
#         return updated_book


# 继承serializers.ModelSerializer
class BooksSerilizers(serializers.ModelSerializer):
    class Meta:
        model = BookView
        fields = '__all__'
        # exclude = ['id', 'pub_date']


# ---------------------------基于APIView的接口实现-----------------------------------------#
# class Book(APIView):
#     # 查-所有
#     # 序列化的过程
#     def get(self, request):
#         # 获取所有书籍
#         book = BookView.objects.all()
#         # 构建序列化器对象
#         res = BooksSerilizers(instance=book, many=True)
#         return Response(res.data)
#
#     # 增
#     # 反序列化的过程
#     def post(self, request):
#         # 获取请求数据
#         # print(request.data)
#         # 构建序列化器对象
#         books = BooksSerilizers(data=request.data)
#         # 校验数据
#         if books.is_valid():
#             # 校验成功，将数据保存到数据库中
#             # BookView.objects.create(**books.validated_data)
#             books.save()
#             return Response(books.data)
#
#         return Response(books.errors)
#
#
# class BookDetailView(APIView):
#     # 查-单个
#     def get(self, request, id):
#         book = BookView.objects.filter(id=id).first()
#         serilizer = BooksSerilizers(instance=book, many=False)
#         return Response(serilizer.data)
#
#     # 改
#     def put(self, request, id):
#         book_edit = BookView.objects.filter(id=id).first()
#         serilizer = BooksSerilizers(instance=book_edit, data=request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data)
#         return Response(serilizer.errors)
#
#     # 删
#     def delete(self, request, id):
#         BookView.objects.filter(id=id).delete()
#         return Response()

# ---------------------------基于GeniricAPIView的接口实现-----------------------------------------#
# from rest_framework.generics import GenericAPIView
#
#
# class Book(GenericAPIView):
#     queryset = BookView.objects.all()
#     serializer_class = BooksSerilizers
#
#     def get(self, request):
#         serializer = self.get_serializer(instance=self.get_queryset(), many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#
# class BookDetailView(GenericAPIView):
#     queryset = BookView.objects.all()
#     serializer_class = BooksSerilizers
#     lookup_field = 'id'
#
#     def get(self, request, id):
#         serializer = self.get_serializer(instance=self.get_object())
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         serializer = self.get_serializer(instance=self.get_object(), data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     def delete(self, request, id):
#         self.get_object().delete()
#         return Response()


# ---------------------------基于Mixins的接口实现-----------------------------------------#
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
#     DestroyModelMixin
#
#
# class Book(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = BookView.objects.all()
#     serializer_class = BooksSerilizers
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class BookDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = BookView.objects.all()
#     serializer_class = BooksSerilizers
#     lookup_field = 'id'
#
#     def get(self, request, id):
#         return self.retrieve(request, id)
#
#     def put(self, request, id):
#         return self.update(request, id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)

# ---------------------------ViewSet类：重构分发机制-----------------------------------------#

# from rest_framework.viewsets import ViewSet
#
# all = {
#     'get': 'get_all',
#     'post': 'add'
# }
#
# one = {
#     'get': 'get_obj',
#     'put': 'update',
#     'delete': 'delete'
# }
#
#
# class Book(ViewSet):
#     def get_all(self, request):
#         return Response('get all')
#
#     def add(self, request):
#         return Response('add')
#
#     def get_obj(self, request,id):
#         return Response('get one')
#
#     def update(self, request,id):
#         return Response('update')
#
#     def delete(self, request,id):
#         return Response('delete')
# ---------------------------GenericViewSet类：重构分发机制且继承GenericView-----------------------------------------#

from rest_framework.viewsets import GenericViewSet

all = {
    'get': 'get_all',
    'post': 'add'
}

one = {
    'get': 'get_obj',
    'put': 'update',
    'delete': 'delete'
}


class Book(GenericViewSet):
    def get_all(self, request):
        return Response('get all')

    def add(self, request):
        return Response('add')

    def get_obj(self, request,id):
        return Response('get one')

    def update(self, request,id):
        return Response('update')

    def delete(self, request,id):
        return Response('delete')
