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
rownames(mat) <- test_files
col_name <- 1: 5
colnames(mat) <- col_name
data.dist=dist.JSD(mat)
rownames(data.dist) <- test_files
colnames(data.dist) <- test_files

data.dist#jensen shanon distance matrix
