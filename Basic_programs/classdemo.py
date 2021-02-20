class A:
    def add(self,a,b):
        self.a = a
        self.b=b
        c=a+b
        print("Addition=",c)
        return c

obj=A()
obj.add(5,2)
