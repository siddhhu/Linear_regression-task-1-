url = "http://bit.ly/w-data"
data=read.csv(url)
data
head(data)
summary(data)
shape(data)
set.seed(2)  #randomize the number #get same number
library(caTools)
split=sample.split(data,SplitRatio = 0.7)
train=subset(data,split="True")
test=subset(data,split="False")
Model=lm(Scores~.,train)
summary(Model)
pred=predict(Model,test)
pred
new=data.frame(Hours=c(9.25))
new
predict(Model, newdata=new)
