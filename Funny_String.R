# Enter your code here. Read input from STDIN. Print output to STDOUT
library(stringr)

nums <- suppressWarnings(readLines(file("stdin")))
nums2<-nums[-1]
asc <- function(x) { strtoi(charToRaw(x),16L) }
strReverse <- function(x)
        sapply(lapply(strsplit(x, NULL), rev), paste, collapse="")
allSame <- function(x) length(unique(x)) == 5
for(i in 1:length(nums2))
    {
    
                   
        nums3<-tolower(str_replace_all(as.matrix(nums2[i]), fixed(" "), ""))
        nums3<-str_replace_all(unlist(strsplit(unlist(nums3),"")),"[^[:alnum:]]", "")
        nums3<-gsub("[^A-Za-z ]", "", nums3)
        nums3<-na.omit(nums3)
        nums4<-length(nums3)
    
        rev1<-strReverse(nums2[i])
        revs3<-tolower(str_replace_all(as.matrix(rev1), fixed(" "), ""))
        revs3<-str_replace_all(unlist(strsplit(unlist(revs3),"")),"[^[:alnum:]]", "")
        revs3<-gsub("[^A-Za-z ]", "", revs3)
        revs3<-na.omit(revs3)
        revs4<-length(revs3)
    
       # write.table(rev1, sep = " ", append=T, row.names = F, col.names = F,quote = FALSE,)

         isFunny<-"Funny"
        for(j in 2:nums4)
               {
                    nums5<-asc(as.character(nums3[j]))
                    nums6<-asc(as.character(nums3[j-1]))
            
                    revs5<-asc(as.character(revs3[j]))
                    revs6<-asc(as.character(revs3[j-1]))
                   # write.table(nums5-nums6, sep = " ", append=T, row.names = F, col.names = F,quote = FALSE,)
                   # write.table(revs5-revs6, sep = " ", append=T, row.names = F, col.names = F,quote = FALSE,)
                    if(abs(nums5-nums6)==abs(revs5-revs6))
                        {
                         funornot<-"Funny"
                        #write.table("Funny", sep = " ", append=T, row.names = F, col.names = F,quote = FALSE,)

                        }
                    else 
                    {
                     funornot<-"Not Funny"
                     isFunny<-"Not Funny"
                     break;
                    }
           
                   
                }
    # write.table(isFunny, sep = " ", append=T, row.names = F, col.names = F,quote = FALSE,)                   
     write.table(funornot, sep = " ", append=T, row.names = F, col.names = F,quote = FALSE,)

        

    }

