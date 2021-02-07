#polymorphism
#more than one form
#polymorphism includes:
#method overloading
#method overriding
#operator overloading

#method overloading
#same method with different number of arguments


class Math:
    def add(self):
        print("No arguments")

    def add(self,num1):
        print("one arguments")

    def add(self,num1,num2):
        print("two arguments")

m=Math()
m.add(10,20)

#In method overloading only the recently implemented methods only works

