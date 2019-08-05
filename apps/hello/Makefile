CC=gcc
NAME=hello
FILES=hello.c
ARGS=

$(NAME): $(FILES)
	$(CC) -o $(NAME) $(FILES)

run: $(NAME)
	./$(NAME) $(ARGS)

.PHONY: clean
clean: $(NAME)
	rm $(NAME)
