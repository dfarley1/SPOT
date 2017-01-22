//-------------------------------------------------------------------------------------------------
//  Auth: David Chalco (0xDC)
//  Desc: The intention of this file is to transfer some file through TCP to the server
//  Date: 01-22-2017
//-------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int clientSocket;
    int com_port;
    char *server_ip;
    char buffer[1024];
    struct sockaddr_in serverAddr;
    socklen_t addr_size;

    // Verify/Parse input
    if(argc < 3) {
        fprintf(stderr, "Usage: ./server port# ip\n");
        exit(1);
    } else {
        com_port = atoi(argv[1]);
        server_ip = argv[2];
    }

    // Create a new socket
    clientSocket = socket(PF_INET, SOCK_STREAM, 0);

    // Configure server settings
    fprintf(stdout, "Configuring server settings:\n\tPORT %d\n\tIP %s\n", com_port, server_ip);
    serverAddr.sin_family = AF_INET;   // Use IP 
    serverAddr.sin_port = htons(com_port);
    serverAddr.sin_addr.s_addr = inet_addr(server_ip);
    memset(serverAddr.sin_zero, '\0', sizeof(serverAddr.sin_zero));

    // Establish socket connection
    fprintf(stdout, "Attempting to connect...\n\n");
    addr_size = sizeof(serverAddr);
    connect(clientSocket, (struct sockaddr*)&serverAddr, addr_size);
    

    // Receive data from server
    recv(clientSocket, buffer, 1024, 0);
    fprintf(stdout, "\t[Server]: %s", buffer);

    // Send data to the server
    memset(buffer,0,sizeof(buffer));
    strcpy(buffer, "This is a message from the client\n");
    send(clientSocket, buffer, strlen(buffer)+1, 0);
    fprintf(stdout, "\t[Client]: %s", buffer);
   
    fprintf(stdout, "\nTransfer complete. Exiting...\n");
    exit(0);
}
