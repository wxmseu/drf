class Animal(object):
    def __init__(self, name, age, func_str):
        self.name = name
        self.age = age
        # self.sleep()
        # 反射
        func = getattr(self, func_str)
        func()

    def sleep(self):
        print('睡觉了')

    def eat(self):
        print("吃饭了")


class Dog(Animal):
    def wangwang(self):
        print('wangwang')

    def sleep(self):
        print('仰天大睡')
class Fly():
    def fly(self):
        print('fly....')

class Bird(Animal,Fly):
    pass

person = Dog('jdq', 19, 'sleep')
bird=Bird('wxm',34,'sleep')
bird.fly()
