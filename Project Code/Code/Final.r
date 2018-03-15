library("tm") 
library("topicmodels")
library("cluster")
library("ade4")
library(SnowballC)
library(LDAvis)
train_folder_path <- "/home/nsk/Desktop/Start/Begin1/Files"
docs <- Corpus(DirSource(train_folder_path,pattern = ".*.txt"))
docs <- tm_map(docs, removePunctuation)#preprocessing
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, tolower)
docs <- tm_map(docs, stemDocument)
docs <- tm_map(docs, stripWhitespace) 
docs <- tm_map(docs, PlainTextDocument)
docs <- tm_map(docs, removeWords, stopwords("SMART"))
dtm <- DocumentTermMatrix(docs)
rowTotals <- apply(dtm , 1, sum) #Find the sum of words in each Document
dtm.new   <- dtm[rowTotals> 0, ]
number_of_topics <- 5
lda <- LDA(dtm.new, k = number_of_topics,method = "Gibbs")#number of topics
#Terms <-get_terms(lda, 5)                         # gets 5 keywords for each topic, just for a quick look
#Topics <-get_topics(lda, 5)



topicmodels_json_ldavis <- function(fitted, corpus, doc_term){
  # Required packages
  library(dplyr)
  library(stringi)
  
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
json <- topicmodels_json_ldavis(lda,docs,dtm.new)
serVis(json, out.dir = 'vis10' )

#The terms in each topic
Terms <- terms(lda, 10)
Terms
write_terms<-function(){
  fileConn1<-file("/home/nsk/Desktop/Start/Begin1/Output/Terms/1.txt","w")
  fileConn2<-file("/home/nsk/Desktop/Start/Begin1/Output/Terms/2.txt","w")
  fileConn3<-file("/home/nsk/Desktop/Start/Begin1/Output/Terms/3.txt","w")
  fileConn4<-file("/home/nsk/Desktop/Start/Begin1/Output/Terms/4.txt","w")
  fileConn5<-file("/home/nsk/Desktop/Start/Begin1/Output/Terms/5.txt","w")
  
  writeLines(Terms[,1],fileConn1)
  writeLines(Terms[,2],fileConn2)
  writeLines(Terms[,3],fileConn3)
  writeLines(Terms[,4],fileConn4)
  writeLines(Terms[,5],fileConn5)
  
  close(fileConn1)
  close(fileConn2)
  close(fileConn3)
  close(fileConn4)
  close(fileConn5)
}
write_terms()

Topics <- topics(lda,2)

colnames(Topics)<-list.files(train_folder_path)

get_files<-function(){
  for(i in 1:length(Topics[1,])){
    if(Topics[i]==1){
      print(paste("1:",colnames(Topics)[i]))
    }
    if(Topics[i]==2){
      print(paste("2:",colnames(Topics)[i]))
    }
    if(Topics[i]==3){
      print(paste("3:",colnames(Topics)[i]))
    }
    if(Topics[i]==4){
      print(paste("4:",colnames(Topics)[i]))
    }
  }
}
Topics <- topics(lda,1)
names(Topics)<-list.files(train_folder_path)
Topics
Topics_Matrix <- matrix(Topics)
file_conn_temp1<-file("/home/nsk/Desktop/Start/Begin1/Output/Associated_Topics/assoc1.txt","w")
file_conn_temp2<-file("/home/nsk/Desktop/Start/Begin1/Output/Associated_Topics/assoc2.txt","w")

file_list<-list.files(train_folder_path)
for(i in 1:length(file_list)){

  writeLines(file_list[i],file_conn_temp1)
  writeLines(paste(Topics_Matrix[i]),file_conn_temp2)

}

close(file_conn_temp1)
close(file_conn_temp2)
Topics_Matrix

#rownames(Topics_Matrix) <- list.files(train_folder_path)
gammaDF <- as.data.frame(lda@gamma) 
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
      resultsMatrix[i,j]=sqrt(JSD(as.vector(inMatrix[i,]),
                                  as.vector(inMatrix[j,])))
    }
  }
  
  return(resultsMatrix) 
}

data.dist=dist.JSD(gammaDF)
rownames(data.dist) <- list.files(train_folder_path)
colnames(data.dist) <- list.files(train_folder_path)
data.dist#janson shanon distance matrix
###################################2nd part##############################
pam.clustering=function(x,k) { # x is a distance matrix and k the number of clusters
  require(cluster)
  cluster = as.vector(pam(as.dist(x), k, diss=TRUE)$clustering)
  return(cluster)
}
number_of_clusters<-5#number of cluster
data.cluster=pam.clustering(data.dist, k=number_of_clusters)

data.cluster
file_list<-list.files(train_folder_path,full.names = TRUE)

write_cluster<-function(){
  fileConn1<-file("/home/nsk/Desktop/Start/Begin1/Output/Clusters/1.txt","w")
  fileConn2<-file("/home/nsk/Desktop/Start/Begin1/Output/Clusters/2.txt","w")
  fileConn3<-file("/home/nsk/Desktop/Start/Begin1/Output/Clusters/3.txt","w")
  fileConn4<-file("/home/nsk/Desktop/Start/Begin1/Output/Clusters/4.txt","w")
  fileConn5<-file("/home/nsk/Desktop/Start/Begin1/Output/Clusters/5.txt","w")

  for(i in 1:length(data.cluster)){
    if (data.cluster[i]==1){
      writeLines(file_list[i],fileConn1)
    }
    if(data.cluster[i]==2){
      writeLines(file_list[i],fileConn2)
    }
    if(data.cluster[i]==3){
      writeLines(file_list[i],fileConn3)
    }
    if(data.cluster[i]==4){
      writeLines(file_list[i],fileConn4)
    }
    if(data.cluster[i]==5){
      writeLines(file_list[i],fileConn5)
    }
  }
  close(fileConn1)
  close(fileConn2)
  close(fileConn3)
  close(fileConn4)
  close(fileConn5)
}

write_cluster()

noise.removal <- function(dataframe, percent=0.01, top=NULL){
  dataframe->Matrix
  bigones <- rowSums(Matrix)*100/(sum(rowSums(Matrix))) > percent 
  Matrix_1 <- Matrix[bigones,]
  print(percent)
  return(Matrix_1)
}
data.denoized=noise.removal(data.dist, percent=0.01)
obs.pca=dudi.pca(data.frame(t(data.dist)), scannf=F, nf=10)
obs.bet=bca(obs.pca, fac=as.factor(data.cluster), scannf=F, nf=number_of_clusters) 
labs <- rownames(obs.bet$ls)
labs
print(obs.bet$ls)
s.class(obs.bet$ls, fac=as.factor(data.cluster), grid=F,col = c(4,2,3,1,5))
text(obs.bet$ls,labels=labs,adj=c(-0.1,-.8),cex=1)

#s.class(obs.bet$ls, fac=as.factor(data.cluster), grid=F, cell=0, cstar=0, col=c(4,2,3))
#########################lastpart#####################################