class Bank{
    deposit(dep){

        this.dep=dep;

    }
    withdraw(drw){
        this.drw=drw;


    }
    balance(bal){
        this.bal=bal

    }
    printdata(){
        console.log(`Deposited Amount:${this.dep} Amount withdrawn:${this.drw} Balance amount:${this.bal}`);
    }
}
var obj=new Bank();
obj.deposit(10000);
obj.withdraw(2000);
obj.balance(8000);
obj.printdata();