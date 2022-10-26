TARGET = semi.out
MAIN = test.c

CC = gcc
#CFLAGS += -g -Wall -std=c99 -MMD -MP -DDEBUG -fPIC
CFLAGS += -g -O2 -foptimize-sibling-calls -Wall -std=c99 -MMD -MP -DDEBUG -fPIC

LINK = gcc
LINKFLAGS = -g

SOURCE_FOLDER = frunzik/src
SOURCES = $(shell find $(SOURCE_FOLDER) -name '*.c')
OBJECTS = $(patsubst %.c, %.o, $(SOURCES))

$(TARGET): $(OBJECTS)
	$(LINK) -o $@ $(OBJECTS) $(MAIN)

%.o : %.c
	$(CC) -c $< -o $@

clean:
	rm $(TARGET)
	rm $(OBJECTS)
