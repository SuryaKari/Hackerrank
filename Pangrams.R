# Enter your code here. Read input from STDIN. Print output to STDOUT
#nums <- scan("stdin",sep=" ")
library(stringr)
library(reshape2)


nums <- read.table("/dev/stdin", sep=" ");
abc<-paste(letters[1:26])
nums2<-tolower(str_replace_all(as.matrix(nums), fixed(" "), ""))
nums3<-str_replace_all(unlist(strsplit(unlist(nums2),"")),"[^[:alnum:]]", "")
nums3<-gsub("[^A-Za-z ]", "", nums3)
nums3<-na.omit(nums3)

nums4<-length(unique(nums3))
#write.table(unique(nums3), sep = "", append=T, row.names = F, col.names = F,quote=F)

#nums3<- strsplit(nums3, "")
if(nums4==26)
    {
        write.table("pangram", sep = "", append=T, row.names = F, col.names = F,quote=F)
    }
if(nums4!=26)
    {
        write.table("not pangram", sep = "", append=T, row.names = F, col.names = F,quote=F)

    }




