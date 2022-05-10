#!/usr/bin/Rscript
args <- commandArgs(T)
library(ggplot2)
data1<-read.table(args[1],header=T)
ggplot(data1)+geom_line(aes(A, hc),color="red",size=2.5)+geom_line(aes(A, cp),color="blue",size=2.5)   +theme_bw()  +scale_x_continuous(breaks=seq(0, 100, 10))  +scale_y_continuous(breaks=seq(-5, 5, 0.1))   +scale_y_continuous(limits = c(-0.5,1.2))
ggsave(args[2])
