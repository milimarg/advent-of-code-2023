FC	=	gfortran

SRC	=	main.f90 \
		galaxymodule.f90 \
		expansionmodule.f90

NAME	=	test

all:
	$(FC) -o $(NAME) $(SRC)

clean:
	rm -f *.o

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
