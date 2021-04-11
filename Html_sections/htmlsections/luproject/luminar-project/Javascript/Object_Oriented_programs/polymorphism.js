//method overloading
//method overloading(same method name and different number of arguements)

class Calculate{
    add(){
        console.log("No arguement method");
    }
    add(num){
        console.log("One arguement method");
    }
    add(num1,num2){
        console.log("Two arguement method");
    }
}

var obj=new Calculate()
obj.add(10);
obj.add(20,10);

