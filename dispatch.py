from multipledispatch import dispatch
class example:
    @dispatch(int, int)
    def add(self, a, b):
        x = a+b
        return x
    @dispatch(int, int, int)
    def add(self, a, b, c):
        x = a+b+c
        return x

class example1(example):
    @dispatch(int, int)
    def add(self, a, b):
        x = a+b
        return x
    @dispatch(int, int, int , int)
    def add(self, a, b, c,d):
        x = a+b+c+d
        return x
obj = example1()
print(obj.add(10,20))
print(obj.add(10,20,30,40))
# print(obj.add(10,20,30))