## 3 x 3 - 2 x 2
library(devtools)
install_github("ramnathv/rblocks")
library(rblocks)

mat <- make_block(3, 3, type = "matrix", )
mat[1:2, 1:2] <- "red"
mat[3,] <- "green"
mat[,3] <- "green"
png(filename = "images/block%d.png")
old_par <- par()
par(bg=NA) 
mat
par(old_par)
dev.off()

# ![image](https://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/block1.png)


