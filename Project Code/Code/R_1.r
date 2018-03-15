topicmodels_json_ldavis <- function(fitted, corpus, doc_term){
  # Required packages
  library(topicmodels)
  library(dplyr)
  library(stringi)
  library(tm)
  library(LDAvis)
  library(jsonlite)
  # Find required quantities
  phi <- posterior(fitted)$terms %>% as.matrix
  theta <- posterior(fitted)$topics %>% as.matrix
  vocab <- colnames(phi)
  doc_length <- vector()
  for (i in 1:length(corpus)) {
    temp <- paste(corpus[[i]]$content, collapse = ' ')
    doc_length <- c(doc_length, stri_count(temp, regex = '\\S+'))
  }
  temp_frequency <- inspect(doc_term)
  freq_matrix <- data.frame(ST = colnames(temp_frequency),
                            Freq = colSums(temp_frequency))
  rm(temp_frequency)
  
  # Convert to json
  json_lda <- LDAvis::createJSON(phi = phi, theta = theta,
                                 vocab = vocab,
                                 doc.length = doc_length,
                                 term.frequency = freq_matrix$Freq)
  return(json_lda)
}
library("tm") 
library("topicmodels")
library("cluster")
library("ade4")
library("jsonlite")
docs <- Corpus(DirSource("/home/nsk/LDA/lda-movie-model/",pattern = ".*.txt"))
summary(docs)   
docs <- tm_map(docs, removePunctuation)  
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, tolower)
library(SnowballC)   
docs <- tm_map(docs, stemDocument)
docs <- tm_map(docs, stripWhitespace) 
docs <- tm_map(docs, PlainTextDocument)
docs <- tm_map(docs, removeWords, stopwords("SMART"))
dtm <- DocumentTermMatrix(docs)
rowTotals <- apply(dtm , 1, sum) #Find the sum of words in each Document
dtm.new   <- dtm[rowTotals> 0, ]
set.seed(357)
t1 <- Sys.time()
num_topics=5
lda <- LDA(dtm.new, k = 5,method = "Gibbs",control = list(alpha = 0.02,iter = 5000,estimate.beta = TRUE))#number of topics

t2 <- Sys.time()
t2 - t1  # about 24 minutes on laptop
json <- topicmodels_json_ldavis(lda,docs,dtm.new)
json_data<-fromJSON(json)# 1
json_data
library(LDAvis)
serVis(json, out.dir = 'vis10')

get_top_results<-function(){
  fileConn1<-file("/home/nsk/Desktop/Start/Begin1/Output/1.txt","w")
  fileConn2<-file("/home/nsk/Desktop/Start/Begin1/Output/2.txt","w")
  fileConn3<-file("/home/nsk/Desktop/Start/Begin1/Output/3.txt","w")
  fileConn4<-file("/home/nsk/Desktop/Start/Begin1/Output/4.txt","w")
  fileConn5<-file("/home/nsk/Desktop/Start/Begin1/Output/5.txt","w")
  
  temp4<-json_data$token.table$Freq
  temp2<-json_data$token.table$Topic
  temp3<-json_data$token.table$Term
  for(i in 1:length(temp4)){
    if(temp2[i]==1 && temp4[i]>0.99){
      writeLines(paste(temp3[i]," ",temp4[i]),fileConn1,sep="\n")
    }
    if(temp2[i]==2 && temp4[i]>0.99){
      writeLines(paste(temp3[i]," ",temp4[i]),fileConn2,sep="\n")
    }
    if(temp2[i]==3 && temp4[i]>0.99){
      writeLines(paste(temp3[i]," ",temp4[i]),fileConn3,sep="\n")
    }
    if(temp2[i]==4 && temp4[i]>0.99){
      writeLines(paste(temp3[i]," ",temp4[i]),fileConn4,sep="\n")
    }
    if(temp2[i]==5 && temp4[i]>0.99){
      writeLines(paste(temp3[i]," ",temp4[i]),fileConn5,sep="\n")
    }
  }
  close(fileConn1)
  close(fileConn2)
  close(fileConn3)
  close(fileConn4)
  close(fileConn5)
}

#get_top_results()
###########################1st part###################################
dist.JSD <- function(inMatrix, pseudocount=0.000001, ...) {
  KLD <- function(x,y) sum(x *log(x/y))
  JSD<- function(x,y) sqrt(0.5 * KLD(x, (x+y)/2) + 0.5 * KLD(y, (x+y)/2))
  matrixColSize <- length(colnames(inMatrix))
  matrixRowSize <- length(rownames(inMatrix))
  colnames <- colnames(inMatrix)
  resultsMatrix <- matrix(0, matrixRowSize, matrixRowSize)
  
  inMatrix = apply(inMatrix,1:2,function(x) ifelse (x==0,pseudocount,x))
  
  for(i in 1:matrixRowSize) {
    for(j in 1:matrixRowSize) { 
      resultsMatrix[i,j]=JSD(as.vector(inMatrix[i,]),
                             as.vector(inMatrix[j,]))
    }
  }
  
  return(resultsMatrix) 
}

doc <- Corpus(DirSource("/home/nsk/Desktop/Start/Begin1/Files",pattern = ".*.txt"))
summary(doc) 
doc <- tm_map(doc, removePunctuation)  
doc <- tm_map(doc, removeNumbers)
doc <- tm_map(doc, tolower)
doc <- tm_map(doc, stemDocument)
doc <- tm_map(doc, stripWhitespace) 
doc <- tm_map(doc, PlainTextDocument)
doc <- tm_map(doc, removeWords, stopwords("SMART"))
dtm2 <- DocumentTermMatrix(doc)
rowTotals <- apply(dtm2 , 1, sum) #Find the sum of words in each Document
dtm2.new   <- dtm2[rowTotals> 0, ]
lda_inf <- posterior(lda,dtm2.new)
lda_inf$topics
mat <- matrix(unlist(lda_inf$topics), ncol = 5, byrow = TRUE)
test_files <- list.files("/home/nsk/Desktop/Start/Begin1/Files")#path of test folder
test_files
rownames(mat) <- test_files
col_name <- 1: 5
colnames(mat) <- col_name
data.dist=dist.JSD(mat)
rownames(data.dist) <- test_files
colnames(data.dist) <- test_files

data.dist#jensen shanon distance matrix
rownames(data.dist)[1]
colnames(data.dist)[3]

###################################2nd part##############################
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

#obs.pca=dudi.pca(data.frame(t(data.dist)), scannf=F, nf=10)
#obs.bet=bca(obs.pca, fac=as.factor(data.cluster), scannf=F, nf=k-1) 
#s.class(obs.bet$ls, fac=as.factor(data.cluster), grid=F)

#s.class(obs.bet$ls, fac=as.factor(data.cluster), grid=F, cell=0, cstar=0, col=c(4,2,3))
#########################lastpart#####################################

obs.pca=dudi.pca(data.frame(t(data.dist)), scannf=F, nf=10)
obs.bet=bca(obs.pca, fac=as.factor(data.cluster), scannf=F, nf=k-1) 
labs <- rownames(obs.bet$ls)
s.class(obs.bet$ls, fac=as.factor(data.cluster), grid=F,col = c(4,2,3,1))
text(obs.bet$ls,labels=labs,adj=c(-0.1,-.8),cex=0.8)

#s.class(obs.bet$ls, fac=as.factor(data.cluster), grid=F, cell=0, cstar=0, col=c(4,2,3))