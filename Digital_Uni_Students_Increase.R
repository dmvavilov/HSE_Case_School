library(readxl)
uni <- read_excel("C:/Users/Митя/Downloads/STEM_DEMAND_SDC_Itog_Restored_1.xlsx")
colnames(uni) <- uni[1,]
uni <- uni[-1,]
seq(1,896, 28) # Названия направлений 
uni <- uni[-seq(1,896, 28),]
uni <- as.data.frame(uni)
uni[uni =="-"] <- 0
for (j in seq(2, 47)){
  uni[,j] <- as.numeric(uni[,j])
}
               
uni_dig <- uni[,c(1,10, 11, 12, 13, 15, 21, 26, 31, 33, 45)]
uni_no_dig <- uni[,-c(1,10, 11, 12, 13, 15, 21, 26, 31, 33, 45)]
# Кол-во бюджетных мест 2015 seq(13, 864, 27) 
# Кол-во бюджетных мест 2016 seq(14, 864, 27) 
# Кол-во бюджетных мест 2017 seq(15, 864, 27) 
# Кол-во бюджетных мест 2018 seq(16, 864, 27)
# Кол-во бюджетных мест 2019 seq(17, 864, 27) 
# Кол-во платных мест 2015 seq(18, 864, 27) 
# Кол-во платных мест 2016 seq(19, 864, 27) 
# Кол-во платных мест 2017 seq(20, 864, 27) 
# Кол-во платных мест 2018 seq(21, 864, 27) 
# Кол-во платных мест 2019 seq(22, 864, 27) 
comp <- data.frame(matrix(nrow = 5, ncol = 4))
rownames(comp) <- c('2015', '2016', '2017', '2018', "2019")
colnames(comp) <- c('Digital_com', 'Digital_bud', 'Not_Digital_com', 'Not_Digital_bud')

for (i in seq(1,5)){
    comp[i,1] <- sum(uni_dig[seq(17+i, 864, 27),seq(2, 11)])
  }
for (i in seq(1,5)){
  comp[i,2] <- sum(uni_dig[seq(12+i, 864, 27),-1])
}
for (i in seq(1,5)){
  comp[i,3] <- sum(uni_no_dig[seq(17+i, 864, 27),-1])
}
for (i in seq(1,5)){
  comp[i,4] <- sum(uni_no_dig[seq(12+i, 864, 27),-1])
}
library(ggplot2)
plot(comp$Digital_com, type='l')
plot.ts(comp)
comp1 <- comp
for (i in seq(2,5)){
  comp[i-1,] <- comp[i,] / comp[i-1,]
}

matplot(comp1, type="b", lty=1, pch=1, col=c("blue", "red", "black", 'green'))
legend('topright', legend = colnames(comp), fill = c("blue", "red", "black", 'green'))

mean(comp[-c(1,5),1])
mean(comp[-c(1,5),3])
mean(comp[-c(1,5),1]) - mean(comp[-c(1,5),3])
# Цифровой ВУЗ растет быстрее не цифрового на 4,7%