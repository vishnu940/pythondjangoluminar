class Student{
    static stddetails(){
        var studentdata={
            1001:{rollno:1001,password:"student1",course:"bca"},
            1002:{rollno:1002,password:"student2",course:"bca"},
            1003:{rollno:1003,password:"student3",course:"mca"},
            1004:{rollno:1004,password:"student4",course:"mca"},
        }
        return studentdata;
    }
    static stdvalidation(rol,passwd){
        var auth=Student.stddetails();
        if(rol in auth){
            if(passwd==auth[rol]["password"]){
                //login success
                return 1;

            }
            else{
                //invalid password
                return 0;
            }
            
        }
        else{
            //invalid roll number
            return -1;
        }

    }
    static stdlogin(){
        var rol=document.querySelector("#roll").value
        var passwd=document.querySelector("#pwd").value
        var res=Student.stdvalidation(rol,passwd);
        if(res==1){
            alert("login successfull");
        }
        else if(res==0){
            alert("invalid password");
        }
        else if(res==-1){
            alert("invalid roll number");
        }
    }
}