CC=gcc
CFLAGS=-Wall --std=c99
DEPS=""
SRC_DIR=./src
BUILD_DIR=./build

client: ${SRC_DIR}/client.c
	${CC} ${CFLAGS} ${SRC_DIR}/client.c -o client
	mkdir -p ${BUILD_DIR}
	mv client ${BUILD_DIR}

server: ${SRC_DIR}/server.c
	${CC} ${CFLAGS} ${SRC_DIR}/server.c -o server
	mkdir -p ${BUILD_DIR}
	mv server ${BUILD_DIR}

clean:
	rm -rf ${BUILD_DIR}
