from api.models import UserToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication


class Authentication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        obj = UserToken.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed('用户认证失败')
        # 在rest framework内部会将整个两个字段赋值给request，以供后续操作使用
        return (obj.user, obj)

