class Company{
    static customedetails(){
        var customerdata={
            1001:{id:1001,password:"customer1",acc_balance:5000},
            1002:{id:1002,password:"customer2",acc_balance:10000},
            1003:{id:1003,password:"customer3",acc_balance:15000},
            1004:{id:1004,password:"customer4",acc_balance:20000},
        }
        return customerdata;


    }
    static authenticate(username,passwd){
        var auth=Company.customedetails();
        if(username in auth){
            if(passwd==auth[username]["password"]){
                return 1;
            }
            else{
                return 0;
            }

        }
        else{
            return -1;
        }

    }
    
    static login(){
        var username=document.querySelector("#uname").value
        var passwd=document.querySelector("#pwd").value
        let user=Company.authenticate(username,passwd);

        if(user==0){
            alert("Incorrect Password");
           
        }
        else if(user==1){
            alert("Login successfull");
            window.location.href="homeproduct.html"
            
            
        }
        else if(user==-1){
            alert("Incorrect Username")
        }

    }
    static buynow(){

        var buy=Company.customedetails();
        var username=document.querySelector("#uname").value
        var passwd=document.querySelector("#pwd").value
        var amount=document.querySelector("#amt").value
        let user=Company.authenticate(username,passwd);
        if(user==0){
            alert("Incorrect password")
        }
        else if(user==1){
            if(amount>buy[username]["acc_balance"]){
                alert("Insufficient balance cannot process transaction");
            }
            else{
                alert("Transaction successfull");
            }
        }
        else if(user==-1){
            alert("Incorrect username");
        }

    }
    static cart(){
        var username=document.querySelector("#uname").value
        var passwd=document.querySelector("#pwd").value
        var amount=document.querySelector("#amt").value
        let user=Company.authenticate(username,passwd);
        if(user==0){
            alert("Incorrect password");
        }
        else if(user==1){
            alert("Item added successfully");
        }
        else if(user==-1){
            alert("Incorrect username");
        }
    }
}