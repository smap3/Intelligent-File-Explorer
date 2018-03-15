library("tm") 
library("topicmodels")
library("cluster")
library("ade4")
library(topicmodels)
library(dplyr)
library(stringi)
library(tm)
library(LDAvis)
library(SnowballC)   

source("R_1.r")
source("R_11.r")

pam.clustering=function(x,k) { # x is a distance matrix and k the number of clusters
  require(cluster)
  cluster = as.vector(pam(as.dist(x), k, diss=TRUE)$clustering)
  return(cluster)
}
k<-5#number of cluster
data.cluster=pam.clustering(data.dist, k=5)

noise.removal <- function(dataframe, percent=0.01, top=NULL){
  dataframe->Matrix
  bigones <- rowSums(Matrix)*100/(sum(rowSums(Matrix))) > percent 
  Matrix_1 <- Matrix[bigones,]
  print(percent)
  return(Matrix_1)
}
data.denoized=noise.removal(data.dist, percent=0.01)

obs.pca=dudi.pca(data.frame(t(data.dist)), scannf=F, nf=10)
obs.bet=bca(obs.pca, fac=as.factor(data.cluster), scannf=F, nf=k-1) 
s.class(obs.bet$ls, fac=as.factor(data.cluster), grid=F)
obs.bet$ls
#s.class(obs.bet$ls, fac=as.factor(data.cluster), grid=F, cell=0, cstar=0, col=c(4,2,3))
#########################lastpart#####################################
