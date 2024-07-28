#자료형
# int, float, str, bool, tuple, set, list, dict
# 시퀀스 자료형 : list, tuple,  str : 연속적인 형태의 자료형

#str immutable 객체, 시퀀스 자료형, 이터러블 객체
# a = "황태영"
# b = "김"
#
# print(b + a[1:])

#tuple #immutable 객체, 시퀀스 자료형, 이터러블 객체
# t = 1,2,3
# for i in t:
#     print(i)

#list #mutable 객체, 시퀀스 자료형, 이터러블 객체

# #dict #mutable 객체,, 이터러블 객체
# d = {
#     1 : "a",
#     2 : "b",
#     3 : "c"
# }
# for i in d:
#     print

# set mutable 객체], 이터러블 객체
# s = {1,2,3,4,5}
# d = {4,5,6,7,8}
#
# print(s ^ d)
# import sys
#
# a = 3
# print(sys.getrefcount(3))

#클로저

# def outter(func):
#     def inner():
#         print('*' * 10)
#         print(func())
#         print('*' * 10)
#
#     return inner
# @outter
# def hello():
#     return 'Hello World!'
#
# #outter(hello())
# hello()

#이터러블, 이터레이터, 제너레이터
#__iter__, __next__
# a = [1,2,3]
# a = iter(a) #이터레이터
# def main():
#     yield 1
#     yield 2
#     yield 3
#
# m = main()
# print(next(m))
# print(next(m))
# print(next(m))

# print(next(a))
# print(next(a))
# print(next(a))

#시퀀스 자료형 : list, tuple, str, range, bytes, bytearray

#인스턴스 메소드, 클래스 메소드, 정적 메소드, 프로퍼티
# class Car:
#     def __init__(self,name,color):    #생성자
#         self.name=name
#         self.color=color
#
#     @staticmethod
#     def window():
#         return "window"
#
#     @property #인스턴스메소드 , 메소드 속성처럼 쓸수있다.
#     def names(self):
#         return self.name
#     @classmethod
#     def wheel(cls):
#         print(cls.window())
#
# audi = Car("Audi","blue")
#
# print(audi.names)

