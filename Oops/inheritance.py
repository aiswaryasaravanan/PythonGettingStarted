#single inheritance

class A:
    def funA1(self):
        print("in funA1")

    def funCommon(self):
        print("in funCommon from A")

class AB(A):
    def funAB1(self):
        print("in funAB1")

    def funCommon(self):
        print("in funCommon from AB")


ab=AB()
ab.funAB1()
ab.funA1()
ab.funCommon()

a=A()
a.funA1()
# a.funAB1()
a.funCommon()

