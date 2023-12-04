NAME	=	test.jar
SRC		=	task01.kt

all:
	kotlinc $(SRC) -include-runtime -d $(NAME)
	java -jar $(NAME) &> test.log
