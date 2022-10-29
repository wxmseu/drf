from rest_framework.throttling import BaseThrottle, SimpleRateThrottle


# import time
# VISIT_RECODE = {}

# class MyThrottle(BaseThrottle):
#     """设置60s内只能访问3次"""
#
#     def __init__(self):
#         self.history = None
#
#     def allow_request(self, request, view):
#         # 获取用户ip
#         remote_addr = request.META.get('REMOTE_ADDR')
#         ctime = time.time()
#         if remote_addr not in VISIT_RECODE:
#             VISIT_RECODE[remote_addr] = [ctime]
#             return True
#         history = VISIT_RECODE.get(remote_addr)
#         self.history = history
#         while history and history[-1] + 60 < ctime:
#             history.pop
#         if len(history) < 3:
#             history.insert(0, ctime)
#             return True
#         return False
#
#     def wait(self):
#         ctime = time.time()
#         return 60 - (ctime - self.history[-1])
class UserThrottle(SimpleRateThrottle):
    scope = 'user'

    # 缓存的key，对于登录用户key为用户名
    def get_cache_key(self, request, view):
        return request.user.username


class VisitorThrottle(SimpleRateThrottle):
    scope = 'visitor'

    # 缓存的key，对于游客用户key为ip
    def get_cache_key(self, request, view):
        return self.get_ident(request)
