# def nice_func(s):
#     return "{} {}".format(s, "have a nice day")
#
#
# print(nice_func("thank you for shopping sir"))
#
#
# def rev(text):
#     print(text[::-1])
#
#
# i = ""
#
# # while i != "q":
# #     i = input("enter a string: ")
# #     rev(i)
#
# text = "i am engineer"
#
# print(text[::-1])
#
# number = [1,2,3,4,5]
#
# print(*number)
#
# print(*"abc")
#
#
#
# def add(x, y):
#     return x + y


def add(*num):
    total = 0
    for n in num:
        total = total + n

    return total


print(add(4, 5, 7))


def about(name, age, likes):
    info = "I am {}. I am {} years old, and I like {}".format(name, age, likes)

    return info


print(about("john", 34, "Python"))
