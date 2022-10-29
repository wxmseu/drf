# class Animal(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # self.sleep()
#         # 反射
#         # func = getattr(self, func_str)
#         # func()
#
#     def sleep(self):
#         print('睡觉了')
#
#     def eat(self):
#         print("吃饭了")
#
#
# class Dog(Animal):
#     def wangwang(self):
#         print('wangwang')
#
#     def sleep(self):
#         print('仰天大睡')
# class Fly():
#     def fly(self):
#         print('fly....')
#
# class Bird(Animal,Fly):
#     pass
#
# # person = Dog('jdq', 19, 'sleep')
# # bird=Bird('wxm',34,'sleep')
# # bird.fly()
# list=[Animal('2',3),Dog('2',3),Bird('2',3)]
# l1=[auth() for auth in list]
# print(l1)
# from rest_framework.authentication import SessionAuthentication
# def func_BMI(name,purpose=22,*args,**kwargs):
#     height=kwargs.pop('height',1.75)
#     weigjt=kwargs.pop('weight',60)
#     bmi=weigjt/height/height
#     print(kwargs)
#     if bmi>purpose:
#         print(name,'太胖了')
#     else:
#         print(name,'太瘦了')
# func_BMI(name='jdq',hh=45)
class A(object):
    def __init__(self, *args, **kwargs):
        print("run the init of A")
    def __new__(cls, *args, **kwargs):
        print("run thr new of A")
        return object.__new__(B, *args, **kwargs)

class B(object):
    def __init__(self):
        print("run the init of B")
    def __new__(cls, *args, **kwargs):
        print("run the new of B")
        return object.__new__(cls)
a = A()
print(type(a))
# b = B()
# print(type(b))