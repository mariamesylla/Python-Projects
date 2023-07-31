def syracuse(n):
    syracuse_str=''
    if(n<1):
        syracuse_str='' 
    elif(n==1):
        syracuse_str='1'  
    else:
        
        syracuse_str=syracuse_str+str(n)+','  
        while(n!=1):  
            if(n%2==0):  
                n=int(n/2)
            else:  
                n=(3*n)+1
            
            if(n==1):  
                syracuse_str=syracuse_str+str(n)+'.'
            else:  
                syracuse_str=syracuse_str+str(n)+','
                
    return(syracuse_str)  

n=int(input('Please enter an  integer : '));

print(syracuse(n))  
