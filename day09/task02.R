filename <- "./input.txt"

lines <- readLines(filename)

calc_layer <- function(array, is_original_array) {
    len <- length(unlist(array))
    temp <- array(0, dim = c(1, (len - 1)))

    for (i in 1:(len - 1)) {
        if (is_original_array) {
            temp[i] <- as.numeric(array[[1]][[i + 1]]) - as.numeric(array[[1]][[i]])
        } else {
            temp[i] <- as.numeric(array[i + 1]) - as.numeric(array[i])
        }
    }


    a <- all(temp == 0)
    if (is.na(a)) {
        return(0)
    } else {
        if (a) {
            return(temp[len - 1])
        }
    }

    output <- calc_layer(temp, 0)

    return(output + temp[len - 1])
}

sum <- 0

for (line in lines) {
    split_line <- strsplit(line, " ")

    len <- length(unlist(split_line))
    for (i in 1:length(split_line)) {
        split_line[[i]] <- as.integer(split_line[[i]])
    }

    split_line <- lapply(split_line, function(x) rev(x))

    result <- calc_layer(split_line, 1) + split_line[[i]]
    sum <- sum + result[len]
}

print(paste("sum =", sum))
