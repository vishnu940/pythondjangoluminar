class Book{
    bookname(name){
        this.name=name;
    }
    bookprice(price){
        this.price=price;
    }
    author(ath){
        this.ath=ath;
    }
    printdetails(){
        console.log("Book Name:" +this.name);
        console.log("Author:" +this.ath);
        console.log("Book price:" +this.price);
    }
}
var obj=new Book()
obj.bookname("Broken Wings");
obj.author("Sarojini Naidu");
obj.bookprice(500);
obj.printdetails();