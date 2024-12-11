CC=g++-13
CPPFLAGS=-g -Wall -Wextra -Wshadow  -Wpedantic -Wconversion -Wnon-virtual-dtor -O3 -std=c++20 #-Werror
SOURCES =solution.cpp
HEADERS =
#DEPS =
all: solution

run: solution
	./solution
solution: $(SOURCES) $(HEADERS)
	$(CC) -o $@ $(SOURCES) $(CPPFLAGS)
clean:
	rm -f solution *~ *.o
