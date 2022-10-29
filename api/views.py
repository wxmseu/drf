from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserInfo, UserToken,UserGroup
from rest_framework import serializers
import hashlib
import time
from api.utils.throttle import VisitorThrottle


def md5(user):
    ctime = str(time.time())
    obj = hashlib.md5()
    obj = hashlib.md5(user.encode('utf-8'))
    obj.update(ctime.encode('utf-8'))
    return obj.hexdigest()


# Create your views here.
class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        # fields=['username']
        fields = '__all__'


class AuthView(APIView):
    """
    登录验证，无需验证，无需要权限
    """
    authentication_classes = []
    permission_classes = []
    throttle_classes = [VisitorThrottle]

    def get(self, request, *args, **kwargs):
        print(request.version)
        # 反向生成url
        u1 = request.versioning_scheme.reverse(viewname='uuu', request=request)
        print(u1)
        # users_info = UserInfo.objects.all()
        # return Response(UserinfoSerializer(instance=users_info, many=True).data)
        return Response('5')

    def post(self, request):
        ret = {'code': 1000, "msg": None}
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            obj = UserInfo.objects.filter(username=username, password=password).first()
            if not obj:
                ret["code"] = 1001
                ret['msg'] = '用户名或者密码错误'
            # 如果登录成功，为用户创建token
            # 若token存在就更新，不存在则创建
            token = md5(username)
            UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token

        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求出错'

        return Response(ret)


# 此处未创建数据库表，用order_dic表示数据库中的表
order_dic = {
    'wxm': {'name': 'mobole', 'price': 18888, 'color': 'red'},
    'jdq': {'name': 'computer', 'price': 18888, 'color': 'white'},
}


class OrderView(APIView):
    """
    订单视图，仅admin用户可以查看
    """

    def get(self, request):
        ret = {'code': 1000, "msg": None, 'data': None}
        ret['data'] = order_dic
        return Response(ret)


from django.core.handlers.wsgi import WSGIRequest


class DjangoView(APIView):
    # authentication_classes = []
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, "msg": None, 'data': None}
        return Response(ret)


# 定义序列化器
from rest_framework import serializers


# class UserViewSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=32)
#     password = serializers.CharField(max_length=32)
#     user_type = serializers.CharField(source='get_user_type_display')
#     group=serializers.CharField(source='group.title')
#     role=serializers.SerializerMethodField() # 对于多对多的详细显示，可用自定义显示，
#     def get_role(self,row):
#         role_obj_list=row.role.all()
#         ret=[]
#         # for item in role_obj_list:
#         #     ret.append({'id':item.id,'title':item.title})
#         for item in role_obj_list:
#             ret.append(item.title)
#         return ret
class UserViewSerializer(serializers.ModelSerializer):
    group=serializers.HyperlinkedIdentityField(view_name='gp',lookup_url_kwarg='xx')
    class Meta:
        model=UserInfo
        fields='__all__'
        # extra_kwargs={
        #     'password':{'min_length':6},
        # }
        depth=1


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        users = UserInfo.objects.all()
        ret = UserViewSerializer(instance=users, many=True,context={'request': request})
        return Response(ret.data)
class GroupViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserGroup
        fields='__all__'

class GroupView(APIView):
    # def get(self, request,pk, *args, **kwargs):
    #     groups=UserGroup.objects.filter(pk=pk).first()
    #     ret=GroupViewSerializer(instance=groups,many=False)
    #     return Response(ret.data)

    def get(self, request, *args, **kwargs):
        pk=kwargs.get('xx')
        groups=UserGroup.objects.filter(pk=pk).first()
        ret=GroupViewSerializer(instance=groups,many=False)
        return Response(ret.data)


class MyValidators:
    def __init__(self, base):
        self.base = base
    # value为用户传来的值
    def __call__(self, value):
        if value != self.base:
            message = 'This field must be %s.' % self.base
            raise serializers.ValidationError(message)

    def set_context(self, serializer_field):
        """
        This hook is called by the serializer instance,
        prior to the validation call being made.
        """
        # 执行验证之前调用,serializer_fields是当前字段对象
        pass

from rest_framework.exceptions import ValidationError
class RoleViewSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=12,error_messages={'required':'标题不能为空'})
    def validate_title(self,data):
        # data就是当前字段的值
        if data!='666':
            print(data)
            raise ValidationError('CHUCUOLE')
        return data


class RoleView(APIView):
    def post(self, request, *args, **kwargs):
        role=RoleViewSerializer(data=request.data)
        if role.is_valid():
            return Response(role.data)
        else:
            return Response(role.errors)
