# Enter your code here. Read input from STDIN. Print output to STDOUT
nums <- scan("stdin",sep=" ")
n<-nums[1] # number of test cases
nums2<-nums[-1]
h<-1 # initial height of tree
t<-1 # test case number
fh<-h
while(t<=n)
{
    fh<-1
    gc<-nums2[t]
    if(gc==0)
        {
            fh<-h
        
        }
    else if(gc==1)
        {
           fh<-h*2
        }
    else if(gc>1)
        {

        for(i in 1:gc)
            {
             if(i%%2!=0)
                 {
                   fh<-fh*2
                 




                 
                 }
            
           if(i%%2 == 0)
                {
                fh<-fh+1
               


                }
            
            }
  
        }
    t<-t+1
      
                            write.table(fh, sep = "", append=T, row.names = F, col.names = F,quote=F)

    

}
