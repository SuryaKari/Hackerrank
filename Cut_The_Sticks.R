


# Enter your code here. Read input from STDIN. Print output to STDOUT
nums <- scan("stdin",sep=" ")
n<-nums[1] # number of sticks
nums2<-nums[-1]
c<-min(nums2)
for(i in 1:n)
    {
        length<-length(nums2[which(nums2>0)])
        write.table(length[which(length>0)], sep = "", append=T, row.names = F, col.names = F,quote=F)
        nums2<-nums2-c
        #write.table(nums2, sep = "", append=T, row.names = F, col.names = F,quote=F)
        nums2<-nums2[which(nums2>0)]   
        c<-min(nums2)
        #write.table(c, sep = "", append=T, row.names = F, col.names = F,quote=F)

    
    }
