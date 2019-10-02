num = -11

print(abs(num))
print(bin(abs(num)))
print(bin(num))
print(sum([1, 2, 3], 4))
print(ascii("a"))
exec("print(num)")
print(eval("1+2"))
print(float(2))
print(format(2, "f"))
print(format(2, "b"))  # formats to binary

i = [0, False, 1]
j = [0, False]
print(all(i))
print(all(j))
print(any(i))
print(any(j))


class A:
    a = 1
    b = ""


obj = A()
print(getattr(obj, "a"))
print(obj.a)

# code_str = 'x=5\ny=10\nprint("sum =",x+y)'
# code = compile(code_str, 'sum.py', 'exec')
# print(type(code))
# exec(code)
