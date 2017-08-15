# Enter your code here. Read input from STDIN. Print output to STDOUT
nums <- suppressWarnings(readLines(file("stdin")))
nums <- as.list(as.data.frame(t(nums)))

p1<-dbinom(3, size=6, prob=109/209)+dbinom(4, size=6, prob=109/209)+dbinom(5, size=6, prob=109/209)+dbinom(6, size=6, prob=109/209)

p2<-signif(p1,digits=3)
write.table(p2, sep = " ", append=T, row.names = F, col.names = F,quote = FALSE,)
