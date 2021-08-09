def func():
    print("Hello World")
func()

def func1(name):
    print("Hi my name is {:s}".format(name))
func1("Henry")

def func3(x,y,z):
    if z:
        return x
    return y

def func4(x,y):
    return x*y

def is_even(n):
    return n%2==0

def greater_than(l,r):
    return l > r

def sum_func(*args):
    return sum(args)

def even_filter(*args):
    ret = []
    for i in args:
        if i % 2 == 0:
            ret.append(i)
    return ret
print(even_filter(7, 6, 11, 5, 29, 4, 11, 17, 32)) 

def spongebob(s):
    ret = ""
    for i in range(0, len(s)):
        if i % 2 == 0:
            ret += s[i].upper()
        else:
            ret += s[i].lower()
    return ret
print(spongebob("This is serious, don't mock me"))
print("         *\n          *\n     ----//-------\n     \..C/--..--/ \   `A\n      (@ )  ( @) \  \// |w\n       \          \  \---/\n        HGGGGGGG    \    /`\n        V `---------`--'\n            <<    <<\n           ###   ###\n")

#"10.Write a function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd." ???????????!??!??!

def string_start(s, t):
    if s[0].lower() == t[0].lower():
        return True
    return False
print(string_start("Test", "turtle"))
print(string_start("miles", "today"))

def func12(i):
    dist_to_7 = abs(7 - i)
    if i > 7:
        return 7 - 2 * dist_to_7
    return 7 + 2 * dist_to_7

print(func12(1))
print(func12(14))

def cap14(s):
    ret = ""
    for i in range(0, len(s)):
        if i == 0 or i == 3:
            ret += s[i].upper()
        else:
            ret += s[i]
    return ret

print(cap14("this is but a test"))

