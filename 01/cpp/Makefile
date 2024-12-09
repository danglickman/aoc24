CC=g++-13
CPPFLAGS=-g -Wall -Wextra -Wshadow  -Wpedantic -Wconversion -Wnon-virtual-dtor -std=c++20 #-Werror
SOURCES =aoc01.cpp
HEADERS =
#DEPS =
all: run

run: aoc01
	../aoc01
aoc01: $(SOURCES) $(HEADERS)
	$(CC) -o ../$@ $(SOURCES) $(CPPFLAGS)
clean:
	rm -f ../aoc01 *~ *.o
