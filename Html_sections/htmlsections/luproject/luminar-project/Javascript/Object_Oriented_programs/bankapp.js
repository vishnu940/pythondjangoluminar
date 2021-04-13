class Bank{
    static bname="sbi";
    constructor(acno,name,bal){
        this.acno=acno;
        this.name=name;
        this.bal=bal;
    }
    deposit(amount){
        this.bal+=amount;
        console.log(`Bank Name:${Bank.bname} Account Number:${this.acno} has been credited with amt${amount} Available balance:${this.bal} `);
    }
    withdraw(amount){
        if(this.bal>amount){
            this.bal-=amount;
            console.log(`Bank Name:${Bank.bname} Account Number:${this.acno} has been debited with amt${amount} Available balance:${this.bal} `);
        
            
        }
        else{
            console.log("Transaction failed Insufficient balance");
        }
      
        
    }
    balance_enquire(){
        console.log(`Available balance:${this.bal}`);
    }

}
var obj1=new Bank(10221544,"Ajay",5000)
obj1.deposit(2000)
obj1.withdraw(1000)
obj1.balance_enquire()

var obj2=new Bank(10236544,"Vijay",10000)
obj2.deposit(5000)
obj2.withdraw(4000)
obj2.balance_enquire()