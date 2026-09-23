# class A :
#     def __init__(self,name):
#         self.__name = name

#     @property
    
#     def name(self):
#         return self.__name

    
# a = A("huzefa")
# print(a.name)

from functools import wraps

def my_wrap(func):
   @wraps(func)
   def nigga(*args, **kwargs):
      print("Hello welcome to decorator")
      func(*args, **kwargs)
   return nigga


@my_wrap
def add (a,b):
   print(a+b)


print(add.__name__)
add(2,4)