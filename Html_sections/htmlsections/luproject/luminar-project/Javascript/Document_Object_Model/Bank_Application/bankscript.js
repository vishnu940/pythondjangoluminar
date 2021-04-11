class Bank{
    
    static accountdetails(){
        var userdata={
            1000:{accno:1000,password:"userone",balance:5000},
            1001:{accno:1001,password:"usertwo",balance:10000},
            1002:{accno:1002,password:"userthree",balance:15000},
            1003:{accno:1003,password:"userfour",balance:20000},
        }
        return userdata;

    }
    
    static authenticate(acno,passwd){
        var dataset=Bank.accountdetails();
        if(acno in dataset){
            if(passwd==dataset[acno]["password"]){
                //login success
                return 1
            }
            else{
                //invalid password
                return 0
            }

        }
        else{
            //invalid account number
            return -1
        }


    }


    static login(){
        var acno=document.querySelector("#acno").value
        var passwd=document.querySelector("#pwd").value
        let user=Bank.authenticate(acno,passwd);
        if(user==0){
            alert("Invalid Password");
        }
        else if(user==1){
            alert("Login Successful");
            window.location.href="home.html"
        }
        else if(user==-1){
            alert("Invalid Account Number");
        }

    }
    static withdraw(){
        var dataset=Bank.accountdetails();
        var acno=document.querySelector("#acno").value
        var passwd=document.querySelector("#pwd").value
        var amount=document.querySelector("#amt").value
        let user=Bank.authenticate(acno,passwd);
        if(user==0){
            alert("Invalid password");
        }
        else if(user==1){
            if(amount>dataset[acno]["balance"]){
                alert("Insufficient balance");
            }
            else{
                alert("Amount Withdrawn");
            }
        }



    }
    static deposit(){
        var acno=document.querySelector("#acno").value
        var passwd=document.querySelector("#pwd").value
        var amount=document.querySelector("#amt").value
        var ath=Bank.authenticate(acno,passwd);
        if(ath==0){
            alert("Invalid password");
        }
        else if(ath==1){
            alert("Amount Deposited");
            
        }
        else if(ath==-1){
            alert("Invalid Account Number");
        }

        
    }
}
