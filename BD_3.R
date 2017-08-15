# Enter your code here. Read input from STDIN. Print output to STDOUT

p1<-pbinom(2, size=10, prob=0.12)
p2<-1-pbinom(1,size=10,prob=0.12)   
write.table(signif(p1,digits=3), sep = " ", append=T, row.names = F, col.names = F,quote = FALSE,)
write.table(signif(p2,digits=3), sep = " ", append=T, row.names = F, col.names = F,quote = FALSE,)