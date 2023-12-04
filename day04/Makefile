NAME	=	test.jar
SRC		=	task02.kt

all:
	kotlinc $(SRC) -include-runtime -d $(NAME)
	java -jar $(NAME) &> test.log
